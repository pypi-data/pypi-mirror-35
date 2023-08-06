#!/usr/bin/env python

""" Replay Overwatch received data as way to test the entire system.

.. codeauthor:: Raymond Ehlers <raymond.ehlers@cern.ch>, Yale University
"""

# Python 2/3 support
from __future__ import print_function
from future.utils import iteritems

# General
import os
import shutil

# Logging
import logging
logger = logging.getLogger(__name__)

# Config
from . import config
(parameters, filesRead) = config.readConfig(config.configurationType.processing)

def replayData():
    pass
