# -*- coding: utf-8 -*-

"""
process module
"""

import sys
import os
import errno
import logging
from datetime import datetime


class Process:
    """
    Run a command with optional arguments in a child process
    Standard output and error from the command can be redirected to an
    optional log file
    """
    # pylint: disable-msg=too-many-instance-attributes
    def __init__(self, command, arguments=None, command_logfile=None):
        """
        Construct a new 'Process' object

        :param command: The command to run
        :param arguments: Optional list of arguments to pass to
                          the command
        :param command_logfile: Optional file to redirect standard
                                output and error from the command
        :return: returns nothing
        """
        self.log = logging.getLogger(__name__)
        self.command = command

        if arguments is None:
            self.arguments = []
        elif isinstance(arguments, list):
            self.arguments = arguments
        else:
            raise Exception('Arguments must be of type list!')

        self.command_logfile = command_logfile
        self.pid = None
        self.exit_code = 255
        # Get original stdout and stderr in case they were modified before
        self.stdout = sys.stdout
        self.stderr = sys.stderr

    def run(self):
        """
        Run the command in a new child process
        Standard output and error from the command are redirected to
        an optional file
        :return: PID of the new child process
        """
        self.log.warning('Starting %s %s', self.command, self.arguments)
        # Fork to run the actual command as a child process
        try:
            self.pid = os.fork()
        except OSError as exc:
            self.log.critical(
                'fork to run process failed: (%s) %s', exc.errno, exc.strerror)
            return None
        if self.pid > 0:
            # Do not exit parent, return to the parent program flow
            return self.pid

        # Redirect standard input file descriptor to /dev/null
        stdin = open('/dev/null', 'r')
        os.dup2(stdin.fileno(), sys.stdin.fileno())

        if self.command_logfile is not None:
            self.log.info('Command logging to %s', self.command_logfile)
            output_file = self.command_logfile
            try:
                with open(self.command_logfile, 'a') as filehandler:
                    filehandler.write(
                        '=== {} STARTING COMMAND: {}{} ===\n'.format(
                            datetime.now(), self.command, self.arguments))
            except IOError as exc:
                self.log.critical(
                    'writing to command logfile %s failed: (%s) %s',
                    self.command_logfile, exc.errno, exc.strerror)
                self.exit_code = os.EX_OSFILE
                # pylint: disable-msg=protected-access
                os._exit(self.exit_code)
        else:
            output_file = '/dev/null'

        # Redirect standard output and error to the configured file
        sys.stdout.flush()
        sys.stderr.flush()
        stdout = open(output_file, 'a')
        stderr = open(output_file, 'a')
        os.dup2(stdout.fileno(), self.stdout.fileno())
        os.dup2(stderr.fileno(), self.stderr.fileno())

        self.log.info('ready to exec command...')
        # Run the command with optional arguments
        # This will substitute the current python child process with the new command
        try:
            os.execvp(self.command, [self.command] + self.arguments)
        except OSError as exc:
            self.log.critical(
                'run process failed: (%s) %s', exc.errno, exc.strerror)
            self.exit_code = os.EX_OSERR
            # pylint: disable-msg=protected-access
            os._exit(self.exit_code)
        return None

    def is_running(self):
        """
        Check if the child process is running
        Save the exit code in case is not running anymore

        :return: True if running, False if not running, None if PID is None
        """
        if self.pid is None:
            self.log.debug('Process pid is unknown')
            return None

        try:
            self.log.debug('Check if child process is running with pid %s',
                           self.pid)
            # Use waitpid to find child process and properly handle it if finished
            pid, status = os.waitpid(self.pid, os.WNOHANG)
            # Transform 16-bits exit code from waitpid() to well-known 8-bits code
            status = status >> 8
            if pid == status == 0:
                self.log.debug('Process is running with pid %s', self.pid)
                return True
            if status == 0:
                self.log.error('Child process %s exited', pid)
            else:
                self.log.critical('Child process %s exited with status %s',
                                  pid, status)
            self.exit_code = status
        except OSError as exc:
            if exc.errno in [errno.ECHILD, errno.ESRCH]:
                self.log.critical('Process with pid %s is not running',
                                  self.pid)
                self.exit_code = 255
            else:
                raise Exception('unhandled errno: %d' % exc.errno)

        self.pid = None
        return False
