import unittest
import pytest
"""
Test for nose2
"""

class Projects(unittest.TestCase):

    def setUp(self):
        """
        Executed for each test
        :return:
        """
        print("Setup")
        # arrange of test
        self.token = "92ae392a6e782dd91578e76dfa1475585d3e2cfa"
        self.headers = {
            "Authorization": "Bearer {}".format(self.token)
        }
        self.url_base = "https://api.todoist.com/rest/v2/projects"

    @classmethod
    def setUpClass(cls):
        """
        Setup class only execute on time
        :return:
        """
        print("Setup Class")

    def test_one(self):
        print("Test one")

    def test_two(self):
        print("Test two")

    def tearDown(self):
        print("teardown")

    @classmethod
    def tearDownClass(cls):
        print("teardown Class")