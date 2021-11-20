import unittest
from workshop4 import User


class UserTests(unittest.TestCase):

    def setUp(self):
        self.user = User('Bob', 1234, 'password')

    def test_user_name(self):
        self.assertEqual(self.user.name, 'Bob')

    def test_user_pin(self):
        self.assertEqual(self.user.pin, 1234)

    def test_user_password(self):
        self.assertEqual(self.user.password, 'password')

    def test_change_name(self):
        self.user.change_name('Robert')
        self.assertEqual(self.user.name, "Robert")
