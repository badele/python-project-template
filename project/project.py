#!/usr/bin/env python
# -*- coding: utf-8 -*-

__authors__ = '{{AUTHOR}} <{{EMAIL}}>'
__copyright__ = 'Copyright (C) {{COPYRIGHTDATE}} {{AUTHOR}}'
__description__ = """{{DESCRIPTION}}"""
__license__ = '{{LICENSE}}'
__version__ = '{{VERSION}}'

import sys
import argparse


def parse_arguments(cmdline=""):
    """Parse the arguments"""

    parser = argparse.ArgumentParser(
        description=__description__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s {version}'.format(version=__version__)
    )

    a = parser.parse_args(cmdline)
    return a


def main():
    # Parse arguments
    args = parse_arguments(sys.argv[1:])  # pragma: no cover


if __name__ == '__main__':
    main()  # pragma: no cover
