# -*- coding: utf-8 -*-
from plone.testing import layered
import robotsuite
import unittest

from collective.ckeditortemplates.testing import CKTEMPLATES_ROBOT_TESTING


def test_suite():
    suite = unittest.TestSuite()
    robot_files = [
        'test.robot',
    ]

    for robot_file in robot_files:
        suite.addTests([
            layered(
                robotsuite.RobotTestSuite(robot_file),
                layer=CKTEMPLATES_ROBOT_TESTING)
        ])
    return suite
