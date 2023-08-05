import pprint

import trio

from ..logmill import _DeferredLog


class Stdout:

    def __init__(self, *args, batch_size=1, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch_size = batch_size

    async def ingest(self, event):
        if isinstance(event, _DeferredLog):
            event_dict = await event()
        else:
            event_dict = event

        pprint.pprint(event_dict)

    async def run(self, task_status=trio.TASK_STATUS_IGNORED):
        # This is simple enough that we don't actually need to do anything.
        task_status.started()
