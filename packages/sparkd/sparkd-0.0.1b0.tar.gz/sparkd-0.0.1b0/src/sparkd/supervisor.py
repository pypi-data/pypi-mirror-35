# -*- coding: utf-8 -*-

"""
supervisor module
"""

import sys
import os
import signal
import errno
import time
import logging


class Supervisor:
    """
    Run, supervise and restart a command defined by the 'Process' object
    """
    # pylint: disable-msg=too-many-arguments
    def __init__(self, process, pidfile,
                 check_interval=1, retries=0, retry_interval=5):
        """
        Construct a new 'Supervisor' object

        :param process: The 'Process' object defining the command to run and
                        supervise
        :param pidfile: The path to a file to save the PID of the process
        :param check_interval: Seconds to wait between checking if the process
                               is still running
        :param retries: Number of times to retry running the command
        :param retry_interval: Seconds to wait before running the command again
        :return: returns nothing
        """
        self.log = logging.getLogger(__name__)
        self.process = process
        self.check_interval = check_interval
        self.retries = retries
        self.retry_interval = retry_interval
        self.pidfile = os.path.abspath(pidfile)
        self.log.debug('Using pidfile %s', self.pidfile)
        self.shutdown = False

    def start(self):
        """
        Start the main control loop to run, supervise and restart the command
        :return: returns nothing
        """
        signal.signal(signal.SIGTERM, self._signal_handler)
        self._control_loop()
        self._cleanup()

    def exit_if_already_running(self):
        """
        Exit the program if a process is already running with the same PID from
        the pidfile
        :return: returns nothing
        """
        pid = self.read_pid()
        if pid and self.pid_running(pid):
            msg = 'Process is already running with pid {}, aborting!'.format(pid)
            self.log.critical(msg)
            sys.stderr.write(msg + '\n')
            sys.exit(1)

    def pid_running(self, pid):
        """
        Check if there is a process running with the same PID from the pidfile
        It checks for any process in the system, not only child processes
        :return: True if running, False if not running
        """
        try:
            self.log.debug(
                'Check if any process is running with pid %s', pid)
            os.kill(pid, 0)
            self.log.debug('Process is running with pid %s', pid)
            return True
        except OSError as exc:
            if exc.errno == errno.ESRCH:
                self.log.debug(
                    'Process with pid %s is not running', pid)
                return False
            if exc.errno == errno.EPERM:
                self.log.debug('No permission to signal the process, assume it is running')
                return True
            raise Exception('unhandled errno: %d' % exc.errno)

    def read_pid(self):
        """
        Get the PID from the pidfile
        :return: PID from the pidfile
        """
        pid = None
        if os.path.isfile(self.pidfile):
            with open(self.pidfile) as filehandler:
                try:
                    pid = int(filehandler.read().strip())
                    self.log.debug('Got pid %s from file %s', pid, self.pidfile)
                except ValueError:
                    pass
        else:
            self.log.debug('No pidfile found %s', self.pidfile)
        return pid

    def write_pid(self, pid):
        """
        Write a PID to the pidfile
        :param pid: The PID to store in the pidfile
        :return: returns nothing
        """
        self.log.info('Writing pid %s to file %s', pid, self.pidfile)
        with open(self.pidfile, 'w') as filehandler:
            filehandler.write('{0}\n'.format(pid))

    def wait_check(self):
        """
        Wait for the time defined as check_interval
        :return: returns nothing
        """
        self.log.debug('Waiting %s seconds to check process', self.check_interval)
        time.sleep(self.check_interval)

    def wait_retry(self):
        """
        Wait for the time defined as retry_interval
        :return: returns nothing
        """
        self.log.info('Waiting %s seconds to restart process', self.retry_interval)
        time.sleep(self.retry_interval)

    def should_restart(self):
        """
        Check if the process is allowed to be restarted again
        :return: True if there are any retries left, False if no retries left
        """
        self.log.info('Restart retries left: %s', self.retries)
        return self.retries > 0

    def _control_loop(self):
        """
        Control loop to run, monitor and restart the command to supervise
        :return: returns nothing
        """
        while not self.shutdown:
            self.log.info('Check process status...')
            is_running = self.process.is_running()

            if is_running is None:
                self.log.info('Process is not running yet, start it...')
                pid = self.process.run()
                self.write_pid(pid)

            elif is_running:
                self.log.info('Process is running, wait to check again...')
                self.wait_check()

            else:
                self.log.info('Process is no longer running')
                if self.should_restart():
                    self.wait_retry()
                    self.retries -= 1
                    # Abort if another process using the same pidfile is already running
                    self.exit_if_already_running()
                else:
                    self.log.critical('Do not try to restart the process again, giving up!')
                    self.shutdown = True

    def _cleanup(self):
        """
        Do cleanup tasks before finishing the supervisor:
        * Try to remove pidfile
        :return: returns nothing
        """
        try:
            self.log.debug('Removing pidfile %s', self.pidfile)
            os.remove(self.pidfile)
        except OSError as exc:
            if exc.errno == errno.ENOENT:
                self.log.warning('Unable to remove missing pidfile %s', self.pidfile)
            else:
                raise Exception('unhandled errno: %d' % exc.errno)

    def _signal_handler(self, signum, frame):
        """
        Handle signals to exit supervisor process
        Kill child process is running
        """
        del frame
        self.shutdown = True
        self.log.warning('Received signal %s, stoping supervisor...', signum)
        pid = self.read_pid()
        if pid and self.pid_running(pid):
            self.log.warning('Killing child process with PID %s...', pid)
            os.kill(pid, signal.SIGTERM)
