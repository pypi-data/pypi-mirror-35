# -*- coding: utf-8 -*-

"""
main module
"""

import sys
import tempfile
import logging
import argparse
from . import __project_name__, __version__
from .sparkd import Sparkd


def main():
    """
    The Sparkd program main method
    """

    def check_positive_int(value):
        """
        Validate a positive integer argparse
        """
        ivalue = int(value)
        if ivalue < 0:
            raise argparse.ArgumentTypeError(
                '%s is an invalid positive int value' % value)
        return ivalue

    def check_positive_float(value):
        """
        Validate a positive float with argparse
        """
        fvalue = float(value)
        if fvalue < 0:
            raise argparse.ArgumentTypeError(
                '%s is an invalid positive float value' % value)
        return fvalue

    parser = argparse.ArgumentParser(
        description='Run any command as a daemon and supervise it'
    )

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        '--version',
        action='store_true',
        help='Show version'
    )

    group.add_argument(
        'command',
        nargs='?',
        help='The command to run as a daemon to supervise'
    )
    parser.add_argument(
        'arguments',
        nargs='*',
        help='Arguments to the command'
    )
    parser.add_argument(
        '-l', '--logfile',
        default=tempfile.gettempdir() + '/sparkd.log',
        help='Set the logfile for the Sparkd supervisor'
    )
    parser.add_argument(
        '--command-logfile',
        default=None,
        help='Set the logfile for the command to supervise'
    )
    parser.add_argument(
        '-n', '--name',
        default=None,
        help='Set the name of this Sparkd instance'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        help='Enable debug logging'
    )
    parser.add_argument(
        '-r', '--retries',
        default=5,
        type=check_positive_int,
        help='Number of retries to restart the process'
    )
    parser.add_argument(
        '-i', '--retry-interval',
        default=5,
        type=check_positive_float,
        help='Seconds to wait between retries to restart the process'
    )
    parser.add_argument(
        '-c', '--check-interval',
        default=1,
        type=check_positive_float,
        help='Seconds to wait between checking process status'
    )

    args = parser.parse_args()

    if args.version:
        print('{} {}'.format(__project_name__, __version__))
        sys.exit(0)

    if args.debug:
        loglevel = logging.DEBUG
    elif args.verbose:
        loglevel = logging.INFO
    else:
        loglevel = logging.WARNING

    sparkd = Sparkd(
        logfile=args.logfile,
        loglevel=loglevel,
        command=args.command,
        arguments=args.arguments,
        name=args.name,
        command_logfile=args.command_logfile,
        retries=args.retries,
        retry_interval=args.retry_interval,
        check_interval=args.check_interval
    )

    sparkd.run()
