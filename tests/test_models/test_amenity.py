#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest

from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime

class TestAmenity(unittest.TestCase):
    """
         Test cases for Amenity class
    """
    created_at = datetime.now()
    updated_at = datetime.now()

    def test_init(self):
        """
        Test for __init__ method
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at)
        self.assertIsInstance(amenity.updated_at)

    def test_amenity_is_subclass(self):
        """
        Test if Amenity is subclass of BaseModel
        """
        amenity = Amenity()
        self.assertTrue(issubclass(amenity.__class__, BaseModel), True)

    def test_name_attr(self):
        """
        Test for name attribute
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
