# Copyright (c) 2018 Red Hat, Inc. and others.  All rights reserved.
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License v1.0 which accompanies this distribution,
# and is available at http://www.eclipse.org/legal/epl-v10.html

import logging
import os
import unittest

from odltools import cli
from odltools import logg
from odltools.common import files
from odltools.karaf import excepts
from odltools.netvirt import tests
from odltools.tests import capture

LOGURL = "https://logs.opendaylight.org/releng/vex-yul-odl-jenkins-1"
JOBNAME = "netvirt-csit-1node-0cmb-1ctl-2cmp-openstack-queens-upstream-stateful-fluorine"


class TestExcepts(unittest.TestCase):
    def setUp(self):
        logg.Logger(logging.INFO, logging.INFO)
        self.logfile = "{}/karaf.excepts.log".format(tests.get_resources_path())
        self.outfile = "/tmp/karaf.excepts.txt"
        self.wlfile = "{}/whitelist.exceptions.netvirt.json".format(tests.get_resources_path())
        self.lines = files.readlines(self.logfile)
        self.num_ex = 3
        self.num_fail = 1
        self.num_match = 2

    def test_get_whitelist(self):
        whitelist = excepts.get_whitelist(self.wlfile)
        self.assertEqual(12, len(whitelist))

    def test_get_exceptions(self):
        exes = excepts.get_exceptions(self.lines)
        # print("exceptions map lines:\n{}".format(exes.keys()))
        self.assertEqual(self.num_ex, len(exes))

    def test_check_exceptions(self):
        exes = excepts.get_exceptions(self.lines)
        # print("exceptions map lines:\n{}".format(exes.keys()))
        self.assertEqual(self.num_ex, len(exes))
        whitelist = excepts.get_whitelist(self.wlfile)
        fails, matches = excepts.check_exceptions(whitelist)
        self.assertEqual(self.num_fail, len(fails))
        self.assertEqual(self.num_match, len(matches))
        # print("\n--->fail list(len={}):\n{}".format(len(fails), fails))
        # print("\n--->match list(len={}):\n{}\n{}".format(len(matches), matches[0].get("issue"),
        #                                                  matches[1].get("issue")))

    def test_verify_exceptions(self):
        whitelist = excepts.get_whitelist(self.wlfile)
        fails, matches = excepts.verify_exceptions(self.lines, whitelist)
        self.assertEqual(self.num_fail, len(fails))
        self.assertEqual(self.num_match, len(matches))

    def test_get_and_verify_exceptions(self):
        excepts.get_and_verify_exceptions(self.logfile, self.outfile, self.wlfile, mode="w")
        self.assertTrue(os.path.isfile(self.outfile))

    def test_get_and_verify_exceptions_for_test(self):
        excepts.get_and_verify_exceptions(
            self.logfile, self.outfile, self.wlfile,
            tname="03 external network.Initial Ping To External Network PNF from Vm Instance 1",
            mode="w")
        self.assertTrue(os.path.isfile(self.outfile))
        self.assertEqual(2, len(files.readlines(self.outfile)))

        excepts.get_and_verify_exceptions(
            self.logfile, self.outfile, self.wlfile,
            tname="02 l3.Connectivity Tests From Vm Instance4 In net_5",
            mode="w")
        self.assertTrue(os.path.isfile(self.outfile))
        self.assertEqual(58, len(files.readlines(self.outfile)))

    def test_cli(self):
        parser = cli.create_parser()
        args = parser.parse_args(["karaf", "exceptions", "--logfile",
                                  self.logfile, "--outfile", self.outfile, "--wlfile", self.wlfile])
        excepts.run(args)
        self.assertTrue(os.path.isfile(self.outfile))
        self.assertEqual(133, len(files.readlines(self.outfile)))

        with capture.capture(excepts.run, args) as output:
            self.assertTrue("IOException: Connection reset by peer" in output)

        args = parser.parse_args(["karaf", "exceptions", "--logfile",
                                  self.logfile, "--outfile", self.outfile, "--wlfile", self.wlfile,
                                  "--testname", "02 l3.Connectivity Tests From Vm Instance4 In net_5",
                                  "--noprint"])
        excepts.run(args)
        self.assertTrue(os.path.isfile(self.outfile))
        self.assertEqual(58, len(files.readlines(self.outfile)))
        with capture.capture(excepts.run, args) as output:
            self.assertTrue(not output)


if __name__ == '__main__':
    unittest.main()
