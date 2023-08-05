'''Logpunch.py contains various bits and pieces meant to duck-punch the
stdlib logging module into submission.

CALL THIS ASAP DURING STARTUP! That way, other modules actually import
our patch, instead of the stdlib, and **all** of the logs actually end
up here.
'''

def patch_stdlib_logging():
    '''This replaces the stdlib logging module with us.'''
