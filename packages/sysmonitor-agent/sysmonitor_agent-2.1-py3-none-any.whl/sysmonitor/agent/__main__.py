#!/usr/bin/env python3
"""
Run sysmonitor agent

It loads command line arguments to load configurations
"""

from sysmonitor.agent.configuration import Configuration
from sysmonitor.agent.interface import BaseInterface

CONFIG = Configuration()
CONFIG.setlog()

INTERFACE = BaseInterface.load(CONFIG)
INTERFACE.start()
