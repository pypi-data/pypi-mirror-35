#!/usr/bin/env python3

########################################################################
#
# test_suite_exsim.py
#
#   Unit test suite for EXSIM
#
# Copyright (C) 2018 EXSIM Development Team (EXSIT)
#
########################################################################

import unittest
import argparse

from test import test_astroenv
from test import test_spacecraft

allTests = False
def parseCmdLineArgs():
    global allTests
    # Note: allow_abbrev is new in version 3.5.
    #parser = argparse.ArgumentParser(allow_abbrev=False)
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--all", help="run all tests",
                        action="store_true")
    args = parser.parse_args()
    if args.all:
        print("Run all tests")
        allTests = True

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(test_astroenv.TestAstroEnv))
    test_suite.addTest(unittest.makeSuite(test_spacecraft.TestPoweredModel))
    test_suite.addTest(unittest.makeSuite(test_spacecraft.TestSpacecraft))
    test_suite.addTest(unittest.makeSuite(test_spacecraft.TestEpsBattery))
    test_suite.addTest(unittest.makeSuite(test_spacecraft.TestEps))
    test_suite.addTest(unittest.makeSuite(test_spacecraft.TestDeployment))
    if allTests:
        pass
    return test_suite

parseCmdLineArgs()
mySuite = suite()
runner=unittest.TextTestRunner()
runner.run(mySuite)

