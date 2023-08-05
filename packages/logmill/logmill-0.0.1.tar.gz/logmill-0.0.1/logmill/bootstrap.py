'''Contains utilities to start and manage the logmill thread (and its
event loop) from the primary application thread.
'''
import threading

import trio

from .logmill import _patch_logmill_call_dunder
from .logmill import _unpatch_logmill_call_dunder


_LOGSRUNNER_THREADLOCK = threading.Lock()
_LOGSRUNNER_INSTANCE = None


class TrioThreadContainer:

    def __init__(self, task, *args, name=None, **kwargs):
        super().__init__(*args, **kwargs)

        # This is what actually gets run
        self._task = task
        # This is the name for the thread
        self._name = name
        # These make sure we only ever have one thread per container
        self._thread = None
        self._threadlock = threading.Lock()
        # These two become threading events
        self._trio_startup = None
        self._trio_shutdown = None
        # These are the trio objects
        self.trio_portal = None
        self._trio_canceller = None

    def __enter__(self):
        with self._threadlock:
            if self._thread is None:
                self._trio_startup = threading.Event()
                self._trio_shutdown = threading.Event()
                self._thread = threading.Thread(target=self._bootstrap_thread,
                                                daemon=False,
                                                name=self._name)
                self._thread.start()
                self._trio_startup.wait()

            else:
                self._trio_startup.wait()

        return self

    def __exit__(self, exc_type, exc, exc_tb):
        try:
            # First we need to make sure the runloop is actually running and
            # its event actually exists
            self._trio_startup.wait()
            # Now we need to kill the root trio task by canceling its cancel
            # scope
            # We want a little bit of insurance in case self._bootstrap_trio
            # somehow errored out before setting this
            if self._trio_canceller is not None:
                try:
                    self.trio_portal.run_sync(self._trio_canceller.cancel)
                # Trio already closed out; suppress any errors since we're just
                # trying to enforce its closure
                except (trio.RunFinishedError, trio.Cancelled):
                    pass

            # Now, we need to wait for the thread to finalize itself. This
            # will get set as the very last thing the thread does
            self._trio_shutdown.wait()
            # And for good measure...
            self._thread.join(timeout=15)

        finally:
            with self._threadlock:
                # Reset everything to its pristine state
                self._thread = None
                self._trio_startup = None
                self._trio_shutdown = None
                self.trio_portal = None
                self._trio_canceller = None

    def _bootstrap_thread(self):
        '''Here we kick off the thread for Trio to run in, and start
        the trio bootstrap.
        '''
        try:
            trio.run(self._bootstrap_trio)
        finally:
            # Set this in case something errored out before it was set in the
            # actual task. It's idempotent, so it doesn't matter if it gets
            # doubled up.
            self._trio_startup.set()
            self._trio_shutdown.set()

    async def _bootstrap_trio(self):
        '''Here we kick off (and eventually cancel) the task for trio
        to run.
        '''
        self.trio_portal = trio.BlockingTrioPortal()

        async with trio.open_nursery() as nursery:
            self._trio_canceller = nursery.cancel_scope
            await nursery.start(self._task)
            # This marks us as started, freeing up __enter__, and then will
            # wait for either self._task to complete, or the nursery to be
            # cancelled via __exit__
            self._trio_startup.set()


class LogsRunner:
    '''LogsRunners enforce a single-instance-globally-per-process limit,
    because having more than one is almost certainly a mistake.
    '''

    def __init__(self, *log_consumers, thread_name=None, filters=None,
                 buffer_capacity=None, shutdown_flush_timeout=None, **kwargs):
        '''Creates a LogsRunner for the passed log_consumers. Each
        log_consumer must work within the logs event loop.

        buffer_capacity controls the internal master buffer. ALL logs
        end up in the master buffer, and are then dispatched to
        individual log consumers, which may then implement their own
        internal buffers.

        TODO: I heard you like buffers, so I put a buffer in your buffer
        because I could but never stopped to consider if I should. Maybe
        we should think a bit more about whether or not it's a good idea
        to just throw all these buffers around willy-nilly; at least
        they're backpressuring each other but it's pretty heavyweight
        for all of these messages.
        '''
        super().__init__(**kwargs)
        self.log_consumers = log_consumers
        self._threadhouse = TrioThreadContainer(task=self._run,
                                                name=thread_name)
        self._master_buffer = None
        # This is for memoization and synchronization sanity. It gets
        # overwritten during __enter__ and restored during __exit__
        self.log = self.logging_disabled

        if filters is None:
            filters = []
        else:
            raise NotImplementedError('Not ready for filters yet!')

        if buffer_capacity is None:
            # Units: number of calls to self.log()
            buffer_capacity = 500

        if shutdown_flush_timeout is None:
            # Units: seconds
            shutdown_flush_timeout = 30

        self.filters = filters
        self.buffer_capacity = buffer_capacity
        self.shutdown_flush_timeout = shutdown_flush_timeout

    @staticmethod
    def logging_disabled(*args, **kwargs):
        '''Use this instead of self.log to indicate that logging is not
        currently active.
        '''
        raise Exception('Logging is currently disabled!')

    async def _run(self, task_status=trio.TASK_STATUS_IGNORED):
        '''This is the task that the TrioThreadContainer actually runs.
        It's the root of the call tree for the logging system.
        '''
        # TODO: need to implement log flushing in try/finally block so that
        # the buffer is always cleared during shutdown
        master_buffer = trio.Queue(capacity=self.buffer_capacity)
        self._master_buffer = master_buffer

        async with trio.open_nursery() as consumer_nursery:
            for log_consumer in self.log_consumers:
                await consumer_nursery.start(log_consumer.run)

            task_status.started()

            try:
                await self._flush_forever(master_buffer, self.log_consumers)

            finally:
                try:
                    with trio.fail_after(self.shutdown_flush_timeout):
                        await self._flush(master_buffer, self.log_consumers)

                except trio.TooSlowError as exc:
                    raise Exception('Logmill timed out while performing ' +
                                    'shutdown flush!') from exc

    @staticmethod
    async def _flush_forever(event_buffer, log_consumers):
        '''Does a flushing in a while loop until the heat death of the
        universe (or until cancellation).
        '''
        while True:
            event_dict = await event_buffer.get()

            for log_consumer in log_consumers:
                await log_consumer.ingest(event_dict)

    @staticmethod
    async def _flush(event_buffer, log_consumers):
        '''Does a flushing in a while loop until the master buffer is
        empty.
        '''
        while not event_buffer.empty():
            event_dict = await event_buffer.get()

            for log_consumer in log_consumers:
                await log_consumer.ingest(event_dict)

    def __enter__(self):
        global _LOGSRUNNER_INSTANCE

        with _LOGSRUNNER_THREADLOCK:
            if _LOGSRUNNER_INSTANCE is None:
                _LOGSRUNNER_INSTANCE = self

            else:
                raise Exception('Running multiple LogsRunner instances ' +
                                'concurrently in the same process is ' +
                                'currently unsupported!')

        self._threadhouse.__enter__()

        # Here, we memoize everything we need for logging, to give things
        # that extra kick in the pants
        run_portal = self._threadhouse.trio_portal.run
        master_buffer_enqueue = self._master_buffer.put

        def log(event_dict, run_portal=run_portal,
                master_buffer_enqueue=master_buffer_enqueue):
            '''The low-level primitive used to dispatch a finalized
            event dict to the log consumers.
            '''
            try:
                run_portal(master_buffer_enqueue, event_dict)
            except (trio.RunFinishedError, trio.Cancelled) as exc:
                # TODO: this needs a way for applications to do something about
                # it, even if that something is a graceful shutdown. I'm
                # imagining a scenario in which this triggers some kind of
                # error cascade in a server, but that doesn't actually kill the
                # server itself because try/catching around Exception in the
                # server block
                raise Exception('Fatal error in logging system! Cannot log! ' +
                                'Bailing out.') from exc

        _patch_logmill_call_dunder(log)
        # This is mostly just useful for testing (lol -- because we *totally*
        # have any tests at all right now)
        self.log = log
        return self

    def __exit__(self, exc_type, exc, exc_tb):
        global _LOGSRUNNER_INSTANCE

        # First disable logging so that the parent caller can't keep issuing
        # logs that may-or-may-not get flushed
        self.log = self.logging_disabled
        _unpatch_logmill_call_dunder()

        try:
            return self._threadhouse.__exit__(exc_type, exc, exc_tb)

        finally:
            with _LOGSRUNNER_THREADLOCK:
                _LOGSRUNNER_INSTANCE = None
                self._master_buffer = None
