#!/usr/bin/python3
"""
    contains the class User
"""
import unittest
from models.base_model import BaseModel
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """
    class TestUser
    """

    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def test_init(self):
        """
        test for init
        """
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime.datetime)
        self.assertIsInstance(user.updated_at, datetime.datetime)

    def test_user_is_subclass(self):
        """
        test for user is subclass
        """
        user = User()
        self.assertTrue(issubclass(user.__class__, BaseModel), True)

    def test_email_attr(self):
        """
        test for email attr
        """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password_attr(self):
        """
        test for password attr
        """
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name_attr(self):
        """
        test for first name attr
        """
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name_attr(self):
        """
        test for last name attr
        """
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

if __name__ == '__main__':
    unittest.main()
