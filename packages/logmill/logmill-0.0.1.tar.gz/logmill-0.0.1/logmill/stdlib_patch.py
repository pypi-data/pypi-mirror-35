'''The sole purpose of patch_stdlib is to import and execute the patch
contained in logpunch. Use it to avoid having your code linters complain
about imports.
'''
from .logpunch import patch_stdlib_logging
patch_stdlib_logging()
