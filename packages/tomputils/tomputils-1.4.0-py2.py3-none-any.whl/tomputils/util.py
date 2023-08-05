# -*- coding: utf-8 -*-
"""
utility functions.

"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import logging
import os
from buffering_smtp_handler import BufferingSMTPHandler
import sys


def exit_with_error(error):
    """
    Log an error and exit after clening up logging.

    I assume that setup_logging() has been called or a global logger variables
    has been set some other way.

    Parameters
    ----------
    error : string
        error message

    Examples
    --------
    >>> from tomputils.util import *
    >>> setup_logging()
    2018-08-04 01:13:36,086;INFO;SMTP logging not configured. [util.py:70]
    >>> exit_with_error("Just testing")
    2018-08-04 01:13:47,271;ERROR;Just testing [util.py:32]
    >>>

    """
    logger.error(error)
    logging.shutdown()
    sys.exit(1)


def get_env_var(var, default=None, secret=False):
    """
    Retrieve an environment variable. A defult may be supplied and will be
    returned if the requested variable is not set. If no default is provided,
    an unset environment variable will considered a fatal error.

    I assume that setup_logging() has been called or a global logger variables
    has been set some other way.

    Parameters
    ----------
    var : string
        variable to find
    default : string, optional
        default returned if variable is unset
    secret : boolean, optional
        if true, do not log value.

    Returns
    -------
    str
        environment variable

    Examples
    --------
    >>> from tomputils.util import *
    >>> setup_logging()
    2018-08-04 01:18:37,519;INFO;SMTP logging not configured. [util.py:99]
    >>> get_env_var("HOME")
    2018-08-04 01:18:41,039;DEBUG;HOME: /Users/tomp [util.py:68]
    '/Users/tomp'
    >>> get_env_var("NOTSET", default="close enough")
    2018-08-04 01:18:44,863;DEBUG;NOTSET: close enough (default) [util.py:76]
    'close enough'
    >>> get_env_var("NOTSET")
    2018-08-04 01:18:51,248;ERROR;Envionment variable NOTSET not set, exiting.
    [util.py:35]
    >>>

    """
    if var in os.environ:
        if not secret:
            logger.debug("%s: %s", var, os.environ[var])
        return os.environ[var]

    else:
        if default is None:
            msg = "Envionment variable {} not set, exiting.".format(var)
            exit_with_error(EnvironmentError(msg))
        else:
            if not secret:
                logger.debug("%s: %s (default)", var, default)
            return default


def setup_logging(subject="Error logs"):
    """
    Setup logging the way I like it. If the following environment variables are
    provided, an email with error level logs will be sent.

    * MAILHOST : where to email logs
    * LOG_SENDER: From: address
    * LOG_RECIPIENT: To: address


    Parameters
    ----------
    subject : string, optional
        subject used if email is generated


    Examples
    --------
    >>> from tomputils.util import *
    >>> logger = setup_logging("Tomp test")
    >>> logger.debug("Test message")
    2018-08-05 12:01:28,577 DEBUG - Test message (<stdin>:1)
    >>> logging.shutdown()
    >>>

    """

    global logger
    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    fmt = "%(asctime)s %(levelname)s - %(message)s (%(filename)s:%(lineno)s)"
    formatter = logging.Formatter(fmt)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    try:
        handler = BufferingSMTPHandler(os.environ['MAILHOST'],
                                       os.environ['LOG_SENDER'],
                                       os.environ['LOG_RECIPIENT'], subject,
                                       1000, fmt)
        handler.setLevel(logging.ERROR)
        logger.addHandler(handler)
        logger.info("SMTP configured, will send email.")
    except KeyError:
        logger.info("SMTP logging not configured.")

    return logger
