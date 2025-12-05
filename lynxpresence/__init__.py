"""
Python RPC Client for Discord
"""

from .baseclient import BaseClient
from .client import AioClient, Client
from .exceptions import *
from .presence import AioPresence, Presence
from .types import ActivityType, StatusDisplayType

__title__ = "lynxpresence"
__author__ = "C0rn3j"
__copyright__ = "Copyright 2018 - 2025"
__license__ = "MIT"
__version__ = "4.6.1"
