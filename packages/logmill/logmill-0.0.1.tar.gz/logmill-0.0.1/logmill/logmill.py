'''Contains the implementation of the core Logmill classes -- Logmill
and Event.
'''
import sys
import weakref

from .stdlib_fallback import get_logger_from_logmill
from .stdlib_fallback import get_loglevel_from_volume


# We use this to infer call information, both upon Logmill creation (to
# eliminate boilerplate like needing to pass __name__ to logging.getLogger)
# and in logmessage creation.
if hasattr(sys, '_getframe'):
    def _get_caller_frame(offset=0):
        # This is faster and more reliable than the inspect module, so use it
        # instead. We know we always want to be up at least two levels, so
        # we're not in our own frame, nor the frame of the function calling
        # this one.
        return sys._getframe(offset + 2)

else:
    def _get_caller_frame(offset=0):
        # This is a bit hacky, but it gets the job done on platforms that don't
        # have sys._getframe.
        try:
            raise ZeroDivisionError

        except ZeroDivisionError as exc:
            frame = exc.__traceback__.tb_frame

        for __ in range(offset + 2):
            frame = frame.f_back

        return frame


def _get_parent_module_name():
    '''Clever way to walk up the stack to get the caller's module name,
    for example package.subpackage. This also normalizes __main__ into
    None.
    '''
    try:
        parent_module_name = _get_caller_frame(offset=1).f_globals['__name__']

    # Stack wasn't deep enough -- we're probably in a REPL; revert to the
    # root logger.
    except ValueError:
        parent_module_name = None

    # Normalize this into the root logger
    if parent_module_name == '__main__':
        parent_module_name = None

    return parent_module_name


# Not entirely sure why we're doing this right now, but hey, I guess it makes
# sense to keep track of all of the instances?
_logmills = weakref.WeakSet()


# These are all the reserved names in events
RESERVED_MAGIC_MSG = '__msg__'
RESERVED_MAGIC_VOL = '__vol__'


class _DeferredLog:

    __slots__ = ['awaitable']

    def __init__(self, awaitable):
        self.awaitable = awaitable


class Event(dict):
    '''Events are dict subclasses that include attributes for any needed
    metadata. Typically, that's a __msg__ and/or a __vol__.
    '''

    def __init__(self, __msg__=None, __vol__=None, *, event_dict):
        '''We use this to convert all of the acceptable call signatures
        from log() into a single format.

        Note that we're keeping the event_dict as a dict to avoid doing
        an extra kwargs expansion.
        '''
        # We don't need to worry about this showing up in both the signature
        # and in **kwargs, because we'd get a TypeError about __init__ getting
        # multiple values for the arg. Therefore, discard anything in the
        # signature if it's already in the kwargs.
        event_dict.setdefault(RESERVED_MAGIC_MSG, __msg__)
        event_dict.setdefault(RESERVED_MAGIC_VOL, __vol__)

        # Do this afterwards so that we always strip those values from the
        # event itself
        super().__init__(**event_dict)

    @property
    def msg(self):
        '''Shorthand for the message.'''
        return self[RESERVED_MAGIC_MSG]

    @property
    def vol(self):
        '''Shorthand for the volume.'''
        return self[RESERVED_MAGIC_VOL]


def _log_via_stdlib_bridge(logmill, *args, **kwargs):
    '''This is assigned as the Logmill class's __call__ method when we
    don't have an active LogsRunner.
    '''

    logger = get_logger_from_logmill(logmill)
    event = Event(*args, event_dict=kwargs)

    # The class definition above ensures these exist in the event, so we don't
    # need to worry about defaults.
    msg = event.pop(RESERVED_MAGIC_MSG)
    vol = event.pop(RESERVED_MAGIC_VOL)

    loglevel = get_loglevel_from_volume(vol)
    # TODO: this needs to subclass so that we don't always have this file as
    # the stack trace!
    logger.log(loglevel, msg, extra=event)


def _patch_logmill_call_dunder(logsrunner_log):
    '''Use this to bind the Logmill class' __call__ to a particular
    logrunner_instance.
    '''

    def __call__(logmill, *args, __logsrunner_log=logsrunner_log, **kwargs):
        '''When we have a LogsRunner instance available, log to it,
        instead of falling back to the stdlib.
        '''
        # Note the partial expansion here!
        event = Event(*args, event_dict=kwargs)
        __logsrunner_log(event)

    Logmill.__call__ = __call__


def _unpatch_logmill_call_dunder():
    '''Use this to restore the stdlib fallback to the Logmill class'
    __call__.
    '''
    Logmill.__call__ = _log_via_stdlib_bridge


class Logmill:

    def __init__(self, *args, **kwargs):
        '''I think this is where we infer the module that's making the
        logger?

        Wait, but what if a module uses multiple loggers?
        '''
        super().__init__(*args, **kwargs)
        _logmills.add(self)
        self.parent_module_name = _get_parent_module_name()

    def defer(self, awaitable):
        self(_DeferredLog(awaitable))

    __call__ = _log_via_stdlib_bridge
