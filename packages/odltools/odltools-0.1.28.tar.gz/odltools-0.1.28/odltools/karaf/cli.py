# Copyright (c) 2018 Red Hat, Inc. and others.  All rights reserved.
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License v1.0 which accompanies this distribution,
# and is available at http://www.eclipse.org/legal/epl-v10.html

import odltools.cli_utils
from odltools.karaf import dump
from odltools.karaf import excepts


def add_dump_parser(parsers):
    parser = parsers.add_parser("format",
                                description="Dump a karaf log with pretty printing of MDSAL objects",
                                help="Dump a karaf log with pretty printing of MDSAL objects")
    parser.add_argument("path", type=odltools.cli_utils.type_input_file,
                        help="Path to karaf log file")
    parser.set_defaults(func=dump.dump_karaf_log)


def add_exceptions_parser(parsers):
    parser = parsers.add_parser("exceptions", description="Process Karaf log exceptions",
                                help="Process Karaf log exceptions")
    parser.add_argument("-o", "--outfile",
                        help="the output file, default: /tmp/karaf.exceptions.txt")
    parser.add_argument("-n", "--noprint", action="store_true",
                        help="do no print the exceptions to stdout")
    parser.add_argument("-l", "--logfile", type=odltools.cli_utils.type_input_file,
                        help="path to a karaf log file, default: /tmp/karaf.log")
    parser.add_argument("-t", "--testname",
                        help="only capture exceptions for the given testname")
    parser.add_argument("-w", "--wlfile",
                        help="the whitelist json file, default: /tmp/whitelist.exceptions.json")
    parser.set_defaults(func=excepts.run)


def add_parser(parsers):
    parser = parsers.add_parser("karaf", description="Karaf log tools")
    subparsers = parser.add_subparsers(dest="subcommand")
    add_dump_parser(subparsers)
    add_exceptions_parser(subparsers)
