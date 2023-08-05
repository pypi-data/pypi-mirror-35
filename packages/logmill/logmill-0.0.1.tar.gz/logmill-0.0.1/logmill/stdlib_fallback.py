'''Well, we really don't want to have to integrate this with the stdlib
logging module, but if you want to use logmill in your packages (and not
just applications) without forcing everyone else to use them too, well,
then I guess we just have to dump things in the stdlib somehow.
'''

import logging

from functools import lru_cache
from logging import NullHandler

# If the message doesn't define a volume level, default to info
DEFAULT_LOGLEVEL = logging.NOTSET
# If we can't infer a name for the logger from the logmill, default to root
DEFAULT_LOGGER = logging.getLogger()

# This is the only place we "enforce" our documented suggested limits,
# (TODO: document those limits!)
# and we do it purely for normalization purposes
MIN_VOLUME = 0
MAX_VOLUME = 100

# When inferring a loglevel from a volume, ...
# ... this is the top end of the scale, ...
LOGLEVEL_INFERRED_CEILING = logging.CRITICAL
# ... this is the bottom end of the scale, ...
LOGLEVEL_INFERRED_FLOOR = logging.DEBUG
# ... and this is the increment to scale by (as an inverse power of 10); ie,
# -1 rounds to nearest 10, 1 rounds to nearest .1, etc
LOGLEVEL_INFERRED_STEP = -1

# (These are calculated based on the above; change them instead!)
_LOGLEVEL_RANGE = LOGLEVEL_INFERRED_CEILING - LOGLEVEL_INFERRED_FLOOR
_LOGLEVEL_SCALE = _LOGLEVEL_RANGE / (MAX_VOLUME - MIN_VOLUME)


@lru_cache()
def get_logger_from_logmill(logmill):
    '''This finds a "best-fit" stdlib logger for the passed Logmill
    instance.
    '''
    parent_module_name = logmill.parent_module_name
    if parent_module_name is not None:
        logger = logging.getLogger(parent_module_name)

        # This prevents warnings about "no handler available for <logger>" when
        # running in code that doesn't necessarily set logging handlers on the
        # root logger -- for example, in test code.
        if not logger.hasHandlers():
            logger.addHandler(NullHandler())

    else:
        logger = DEFAULT_LOGGER

    return DEFAULT_LOGGER


def get_loglevel_from_volume(volume):
    '''This finds a "best-fit" loglevel for the passed log volume level.
    '''
    if volume is None:
        return DEFAULT_LOGLEVEL

    volume = min(volume, MAX_VOLUME)
    volume = max(volume, MIN_VOLUME)

    scaled_volume = _LOGLEVEL_SCALE * volume
    offset_volume = scaled_volume + LOGLEVEL_INFERRED_FLOOR
    return int(round(offset_volume, LOGLEVEL_INFERRED_STEP))
