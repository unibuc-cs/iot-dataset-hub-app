"""
    SmartTV-Alpha

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import smarttv
from smarttv.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_channel_username_canal_post(self):
        """Test case for add_channel_username_canal_post

        """
        pass

    def test_get_history_and_recommandations_nume_get(self):
        """Test case for get_history_and_recommandations_nume_get

        """
        pass

    def test_get_suggested_channels_gen_varsta_get(self):
        """Test case for get_suggested_channels_gen_varsta_get

        """
        pass

    def test_get_users_get(self):
        """Test case for get_users_get

        """
        pass

    def test_get_users_json_get(self):
        """Test case for get_users_json_get

        Loads users into output_users.json file.  # noqa: E501
        """
        pass

    def test_insert_user_username_varsta_post(self):
        """Test case for insert_user_username_varsta_post

        """
        pass

    def test_notification_distance_size_current_distance_get(self):
        """Test case for notification_distance_size_current_distance_get

        """
        pass

    def test_set_brightness_level_post(self):
        """Test case for set_brightness_level_post

        """
        pass

    def test_set_brightness_our_sensor_post(self):
        """Test case for set_brightness_our_sensor_post

        Loads brightness from (another) file.  # noqa: E501
        """
        pass

    def test_set_brightness_sensor_post(self):
        """Test case for set_brightness_sensor_post

        Loads brightness from file.  # noqa: E501
        """
        pass

    def test_timp_idle_time_post(self):
        """Test case for timp_idle_time_post

        """
        pass

    def test_timp_last_get(self):
        """Test case for timp_last_get

        """
        pass

    def test_timp_start_get(self):
        """Test case for timp_start_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
