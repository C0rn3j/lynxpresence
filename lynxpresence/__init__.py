"""
Python RPC Client for Discord
"""

from .baseclient import BaseClient
from .client import Client, AioClient
from .exceptions import *
from .types import ActivityType
from .presence import Presence, AioPresence


__title__ = 'lynxpresence'
__author__ = 'C0rn3j'
__copyright__ = 'Copyright 2018 - 2025'
__license__ = 'MIT'
__version__ = '4.4.1'
