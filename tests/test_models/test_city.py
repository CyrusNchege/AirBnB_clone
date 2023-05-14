#!/usr/bin/python3
"""
Unittest for city 
"""
import unittest

from models.city import City
from models.base_model import BaseModel
from datetime import datetime

class TestCity(unittest.TestCase):
    """
    Test cases for city class
    """
    created_at = datetime.now()
    updated_at = datetime.now()

    def test_init(self):
        """
        Test for __init__ method
        """
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at)
        self.assertIsInstance(city.updated_at)

    def test_city_is_subclass(self):
        """
        Test if city is subclass of BaseModel
        """
        city = city()
        self.assertTrue(issubclass(city.__class__, BaseModel), True)

    def test_name_attr(self):
        """
        Test for name attribute
        """
        city = city()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
    
    def test_state_id_attr(self):
        """
        Test for state_id attribute
        """
        city = city()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_two_models_unique_ids(self):
        """
        Test for unique id
        """
        city = City()
        city1 = City()
        self.assertNotEqual(city.id, city1.id)
    
    def test_str(self):
        """
        Test for __str__ method
        """
        city = City()
        city.name = "Nairobi"
        city.my_number = 254
        expected = "[City] ({}) {}".format(
            city.id, 
            city.__dict__
            )
        self.assertEqual(expected, str(city))

    def test_save(self):
        """
        Test for save method
        """
        city = City()
        city.save()
        self.assertTrue(city.updated_at, datetime)(city.updated_at)
        self.assertNotEqual(city.created_at, city.updated_at)
    
    def test_to_dict(self):
        """
        Test for to_dict method
        """
        city = City()
        city.name = "Nairobi"
        city.my_number = 254
        expected_dict  = {
            "id": city.id,
            "name": "Nairobi",
            "my_number": 254,
            "__class__": "City",
            "created_at": city.created_at.isoformat(),
            "updated_at": city.updated_at.isoformat()
        }
        self.assertEqual(expected_dict, city.to_dict())

    

if __name__ == "__main__":
    unittest.main()
