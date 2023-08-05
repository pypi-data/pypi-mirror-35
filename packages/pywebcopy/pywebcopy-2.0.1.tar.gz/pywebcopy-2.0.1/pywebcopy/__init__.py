# -*- coding: utf-8 -*-

"""
aerwebcopy
~~~~~~~~~~

A pythonic library to mirror any online website as is.
It respects robots.txt

"""

from __future__ import absolute_import

__author__ = 'Raja Tomar'
__copyright__ = 'Copyright Aeroson Systems & Co.'
__license__ = 'Licensed under MIT'
__email__ = 'rajatomar788@gmail.com'
__package__ = 'pywebcopy'


import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from pywebcopy import core
from pywebcopy import structures
from pywebcopy import config
from pywebcopy import utils
from pywebcopy import generators
from pywebcopy import exceptions


__version__ = config.config['version']


__all__ = [
    '__version__', '__author__', '__copyright__', '__license__', '__email__',
    'core', 'structures', 'config', 'utils', 'generators', 'exceptions'
]


