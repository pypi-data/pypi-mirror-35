# -*- coding: utf-8 -*-

"""
daemon module
"""

import sys
import os
import logging
from . import logger


def daemonize():
    """
    According to Stevens's Advanced Programming in the UNIX Environment
    chapter 13, this is the procedure to make a well-behaved Unix daemon:

    Fork and have the parent exit. This makes the shell or boot script
    think the command is done. Also, the child process is guaranteed not
    to be a process group leader (a prerequisite for setsid next)

    Call setsid to create a new session. This does three things:
    * The process becomes a session leader of a new session
    * The process becomes the process group leader of a new process group
    * The process has no controlling terminal

    Fork again and have the parent exit. This guarantes that the daemon
    is not a session leader nor can it acquire a controlling terminal
    """
    log = logging.getLogger(__name__)
    log.debug('Doing first fork to become a daemon...')
    try:
        pid = os.fork()
        if pid > 0:
            # Exit first parent using os._exit() instead of sys.exit()
            # to avoid flushing I/O and triggering handlers
            # pylint: disable-msg=protected-access
            os._exit(0)
    except OSError as exc:
        log.critical('fork #1 failed: (%s) %s', exc.errno, exc.strerror)
        sys.exit(1)

    # decouple from parent environment
    os.chdir('/')
    os.setsid()
    os.umask(0)

    log.debug('Doing second fork to become a daemon...')
    try:
        pid = os.fork()
        if pid > 0:
            # Exit second parent using os._exit() instead of sys.exit()
            # to avoid flushing I/O and triggering handlers
            # pylint: disable-msg=protected-access
            os._exit(0)
    except OSError as exc:
        log.critical('fork #2 failed: (%s) %s', exc.errno, exc.strerror)
        sys.exit(1)

    # Redirect standard input file descriptor to /dev/null
    stdin = open('/dev/null', 'r')
    os.dup2(stdin.fileno(), sys.stdin.fileno())

    # Redirect standard output and error file descriptors to logging function
    sys.stdout.flush()
    sys.stderr.flush()
    sys.stdout = logger.StreamToLogger(log, logging.INFO)
    sys.stderr = logger.StreamToLogger(log, logging.WARNING)

    return os.getpid()
