"""
    SmartKettle

    App that controls an smart electric kettle. Part of the IoT-dataset for fuzzing Smart Home Appliances.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import smartkettle
from smartkettle.model.make_tea_temperature import MakeTeaTemperature
globals()['MakeTeaTemperature'] = MakeTeaTemperature
from smartkettle.model.inline_object1 import InlineObject1


class TestInlineObject1(unittest.TestCase):
    """InlineObject1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineObject1(self):
        """Test InlineObject1"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InlineObject1()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
