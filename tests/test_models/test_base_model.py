#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import os


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """
    def test_init(self):
        """
        Test for __init__ method
        """
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertTrue(b1.id, str)(b1.id)
        self.assertTrue(b1.created_at, datetime)(b1.created_at)
        self.assertTrue(b1.updated_at, datetime)(b1.updated_at)

    def test_str(self):
        """
        Test for __str__ method
        """
        b1 = BaseModel()
        self.assertIsInstance(b1.__str__(), str)
        
    def test_save(self):
        """
        Test for save method
        """
        b1 = BaseModel()
        b1.save()
        self.assertTrue(b1.updated_at, datetime)(b1.updated_at)
        self.assertNotEqual(b1.created_at, b1.updated_at)

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        self.assertIsInstance(b1_dict, dict)
        self.assertIsInstance(b1_dict['created_at'], str)
        self.assertIsInstance(b1_dict['updated_at'], str)
        self.assertEqual(b1_dict['__class__'], 'BaseModel')

    def test_kwargs(self):
        """
        Test for kwargs
        """
        b1 = BaseModel()
        b1.name = "Holberton"
        b1.my_number = 89
        b1_dict = b1.to_dict()
        b2 = BaseModel(**b1_dict)
        self.assertEqual(b1.id, b2.id)
        self.assertEqual(b1.created_at, b2.created_at)
        self.assertEqual(b1.updated_at, b2.updated_at)
        self.assertEqual(b1.name, b2.name)
        self.assertEqual(b1.my_number, b2.my_number)
        self.assertNotEqual(b1, b2)


if __name__ == '__main__':
    unittest.main()
