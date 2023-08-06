#!/usr/bin/env python

""" Handle and move files from the receiver(s).

We take a simple approach of determine which files to transfer, and then moving them to the
appropriate locations. We could try to use something like ``watchdog`` to do something more
clever when a file changes. However, we want to batch transfer files to take advantage of
``rsync``, so such an approach would require much more complicated bookkeeping (for example,
what happens if a file shows up when transferring data, etc). The much simpler approach that
we use solves our problem just as well, but is also much easier to write and maintain.

.. codeauthor:: Raymond Ehlers <raymond.ehlers@cern.ch>, Yale University
"""

# Python 2/3 support
from __future__ import print_function
from future.utils import iteritems

# General
import os
import math
import time
import shutil
import functools

import ROOT

# Logging
import logging
logger = logging.getLogger(__name__)

# Config
from . import config
(parameters, filesRead) = config.readConfig(config.configurationType.processing)

def retry(tries, delay = 3, backoff = 2):
    """Retries a function or method until it returns True.

    # Retry decorator with exponential backoff

    delay sets the initial delay in seconds, and backoff sets the factor by which
    the delay should lengthen after each failure. backoff must be greater than 1,
    or else it isn't really a backoff. tries must be at least 0, and delay
    greater than 0.

    Original decorater from the `Python wiki <https://wiki.python.org/moin/PythonDecoratorLibrary#Retry>`__,
    and using some additional improvemnts `here <https://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/>`__.

    Args:
        tries (int):
        delay (int):
        backoff (int):
    Returns:
        bool: True if the function succeeded.
    """
    # Argument validation
    if backoff <= 1:
        raise ValueError("Backoff must be greater than 1")
    tries = math.floor(tries)
    if tries < 0:
        raise ValueError("Tries must be 0 or greater")
    if delay <= 0:
        raise ValueError("Delay must be greater than 0")

    def deco_retry(f):
        @functools.wraps(f)
        def f_retry(*args, **kwargs):
            # make mutable
            mtries, mdelay = tries, delay

            # First attempt at calling the function
            rv = f(*args, **kwargs)
            while mtries > 0:
                # If we ever get a return value of `True`, we are done.
                if rv is True:
                    return True

                # Setup for the next attempt and wait before the next attempt
                mtries -= 1
                time.sleep(mdelay)
                mdelay *= backoff

                # Try again
                rv = f(*args, **kwargs)

            # Ran out of tries. Return failure.
            return False

        # true decorator -> decorated function
        return f_retry
    # @retry(arg[, ...]) -> true decorator
    return deco_retry

# TODO: Tune these parameters a bit!
@retry(tries = 3)
def copyFileToEOSWithRoot(filename):
    """ Copy a given file to EOS using ROOT capabilities.

    ...

    Args:
        filename (str): Local filename of the string to be copied. This will be used for setting
            the path where it will be copied.
    Returns:
        bool: True if the file was copied successfully
    """
    destiation = os.path.join(parameters["eosDirPrefix"], filename)
    # We only want to see such information if we are debugging. Otherwise, it will just clog up the logs.
    showProgressBar = parameters["debug"]
    return ROOT.TFile.Cp(filename, destiation, showProgressBar)

def copyFilesToEOS(filenames):
    """ Copy the given filenames to EOS.

    ...

    Args:
        filenames (list): Paths to files to copy to EOS.
    Returns:
        list: Filenames for all of the files which failed.
    """
    failedFilenames = []
    for f in filenames:
        # This function will automatically retry.
        res = copyFileToEOSWithRoot(f)
        # Store the failed files so we can notify the admin that something went wrong.
        if res is False:
            failedFilenames.append(f)

    return failedFilenames

def determineFilesToMove():
    """ Determine the files which are available to be moved or otherwise transferred.

    Since there could be additional directories which we want to ignore, we want to use avoid
    using ``os.walk()``, which will include subdirectories. Instead, we use a simpler solution
    with ``os.listdir()`` and verify that we include only files.

    Args:
        None
    Returns:
        list: List of the files available to be moved.
    """
    return [f for f in os.listdir(parameters["receiverData"]) if os.path.isfile(f)]

# Steps:
# - Enumerate the available files.
# - rsync the files to other sites.
#   - Somehow signal that we have new files. Touch a file? Write what was transferred?
# - Copy those files to EOS.
# - If both of the above were successful, then delete the local files
# - Otherwise, move the unsuccessful files to another directory to keep them around. Still delete any successful files

def processReceivedFiles():
    """ Main driver function for receiver file processing

    Note:
        Configuration is controlled via the Overwatch YAML configuration system. In particular,
        the options relevant here are defined in the base module.

    Args:
        None.
    """
    # These are just raw filenames.
    filenames = determineFilesToMove()

    # Copy files via rsync
    rsyncFailedFilenames = copyFilesToOverwatchSites(filenames)

    # Copy files to EOS
    eosFailedFilenames = copyFilesToEOS(filenames)

    # Notify the Overwatch sites about the new files

    # Determine the definitive set of failed files
    # NOTE: We shouldn't have any duplicate filenames, so set shouldn't
    #       do anything beyond making it possible to call union
    failedFilenames = set(rsyncFailedFilenames) | set(eosFailedFilenames)

    # Only delete files if none have failed.
    if failedFilenames:
        # Move to a safer location
        for f in failedFilenames:
            # TODO: Define this directory in parameters
            shutil.move(f, os.path.join(parameters["tempStorageData"], f))

        # TODO: Notify the admin, etc
        pass

    # Determine which files we can safely remove
    removableFilenames = set(filenames) - set(failedFilenames)

    if failedFilenames:
        # Sanity check
        assert len(filenames) == len(removableFilenames) + len(failedFilenames)

    # Protect from data loss when testing
    if parameters["debug"] is False:
        for f in filenames:
            os.remove(f)

# TODO: Add some monitoring information and send summary emails each day. This way, I'll know that
#       Overwatch is still operating properly.
