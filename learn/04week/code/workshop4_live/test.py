import unittest
from workshop4 import *


class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.user = User('Bob', 1234, 'password')

    def test_user_name(self):
        self.assertEqual(self.user.name, 'Bob')

    def test_user_pin(self):
        self.assertEqual(self.user.pin, 1234)

    def test_user_pasword(self):
        self.assertEqual(self.user.password, 'password')
