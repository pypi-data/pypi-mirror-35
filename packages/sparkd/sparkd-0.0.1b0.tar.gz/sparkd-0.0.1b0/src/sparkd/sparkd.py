# -*- coding: utf-8 -*-

"""
sparkd module
"""

import tempfile
import logging
from . import logger
from . import daemon
from .supervisor import Supervisor
from .process import Process


class Sparkd:
    """
    Create a 'Supervisor' instance to run, supervise and restart a
    command defined by a 'Process' object
    """
    # pylint: disable-msg=too-few-public-methods
    pidfile_dir = tempfile.gettempdir()
    pidfile_template = '{dir}/sparkd-{name}.pid'

    # pylint: disable-msg=too-many-arguments
    def __init__(self, command, arguments=(), command_logfile=None, name=None,
                 logfile=None, loglevel=logging.WARNING,
                 check_interval=1, retries=0, retry_interval=5):
        """
        Construct a new 'Sparkd' object

        :param command: The command to run, supervise and restart
        :param arguments: Optional list of arguments to pass to the
                          command
        :param command_logfile: Optional file to redirect standard
                                output and error from the command
        :param name: A unique name for this Sparkd supervisor instance,
                     used to define the pidfile name
        :param logfile: Optional file to redirect standard output and
                        error from the supervisor
        :param loglevel: The log level to configure the logger object
        :param check_interval: Seconds to wait between checking if the
                               process is still running
        :param retries: Number of times to retry running the command
        :param retry_interval: Seconds to wait before running the
                               command again
        :return: returns nothing
        """
        logger.setup(logfile, loglevel)
        self.log = logging.getLogger(__name__)

        self.log.debug('Configure process...')
        process = Process(
            command=command,
            arguments=arguments,
            command_logfile=command_logfile
        )

        if name is None:
            self.name = command
        else:
            self.name = name
        pidfile = self.pidfile_template.format(
            dir=self.pidfile_dir,
            name=self.name.replace('/', '_')
        )

        self.log.debug('Configure sparkd supervisor...')
        self.supervisor = Supervisor(
            process=process,
            retries=retries,
            retry_interval=retry_interval,
            check_interval=check_interval,
            pidfile=pidfile
        )

    def run(self):
        """
        Run a Sparkd supervisor instance
        1. Abort if a process using the same pidfile is already running
        2. Become a daemon
        3. Start the supervisor to run, monitor and restart the command
        :return: returns nothing
        """
        self.supervisor.exit_if_already_running()
        self.log.debug('Become a daemon...')
        daemon.daemonize()
        self.log.debug('Start supervisor...')
        self.supervisor.start()
