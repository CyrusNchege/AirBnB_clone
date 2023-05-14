#!/usr/bin/python3
"""
    test for place
"""
from models.place import Place
from models.base_model import BaseModel

import unittest
from datetime import datetime


class TestPlace(unittest.TestCase):
    """ 
    test for place 
    """
    created_at = datetime.now()
    updated_at = datetime.now()

    def test_init(self):
        """ 
        test for init 
        """
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)

    def test_place_is_subclass(self):
        """ 
        test for place is subclass 
        """
        place = Place()
        self.assertTrue(issubclass(place.__class__, BaseModel), True)

    def test_city_id_attr(self):
        """ 
        test for city id attr 
        """
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")
    
    def test_user_id_attr(self):
        """ 
        test for user id attr 
        """
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")
    
    def test_name_attr(self):
        """ 
        test for name attr 
        """
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")


    def test_description_attr(self):
        """ 
        test for description attr 
        """
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_number_rooms_attr(self):
        """ 
        test for number rooms attr 
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)
    
    def test_number_bathrooms_attr(self):
        """ 
        test for number bathrooms attr 
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """ 
        test for max guest attr 
        """
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night_attr(self):
        """ 
        test for price by night attr 
        """
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)
    
    def test_latitude_attr(self):
        """ 
        test for latitude attr 
        """
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place.latitude, 0.0)
    
    def test_longitude_attr(self):
        """ 
        test for longitude attr 
        """
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place.longitude, 0.0)
    
    def test_amenity_ids_attr(self):
        """ 
        test for amenity ids attr 
        """
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.amenity_ids, [])

    def test_to_dict_creates_dict(self):
        """
        test to_dict method creates a dictionary with proper attrs
        """
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in p.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)
        
    def test_str(self):
        """
        test str method
        """
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))
    
    def test_unique_ids(self):
        """
        test unique ids
        """
        place = Place()
        place_2 = Place()
        self.assertNotEqual(place.id, place_2.id)

    def test_save(self):
        """
        test save method
        """
        place = Place()
        place.save()
        self.assertNotEqual(place.created_at, place.updated_at)
