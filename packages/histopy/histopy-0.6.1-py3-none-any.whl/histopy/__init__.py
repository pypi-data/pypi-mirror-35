'''
BASH-style history for the Python3 interactive interpreter.

Quickstart: 
>>> import histopy as hp
>>> hp.history_full()     # like $ history
>>> hp.history()          # history of current session
>>> hp.recall(n)          # like $ !n
'''

from .hp import *

__all__ = (
        'history', 'history_full', 'recall', 'recall_range', 'find'
        '__title__', '__summary__', '__url__', '__version__', '__author__',
        '__email__', '__license__'
        )

__title__ = 'histopy'
__summary__ = 'Command line history for Python interactive interpreter'
__url__ = 'https://github.com/dwpaley/histopy'
__version__ = '0.6.1'
__author__ = 'Daniel W. Paley'
__email__ = 'dwpaley@gmail.com'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2018 Daniel W. Paley'
