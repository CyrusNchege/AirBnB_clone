#!/usr/bin/python3  
"""
    Test cases for file storage
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State  
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """"
        Test cases for file storage
    """
    def test_save_method_creates_file(self):
        """
        Test for save method
        """
        new = BaseModel()
        self.storage.new(new)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def setUp(self):
        """
        Setup for test
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Remove test instances
        """
        del self.storage

    def test_file_path(self):
        """
        Test for file path
        """
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        """
        Test for objects
        """
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_all(self):
        """
        Test for all method
        """
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """
        Test for new method
        """
        self.storage.new(User())
        self.storage.new(City())
        self.storage.new(State())
        self.storage.new(Place())
        self.storage.new(Amenity())
        self.storage.new(Review())
        self.assertIsInstance(self.storage.all(), dict)

    def test_save(self):
        """
        Test for save method
        """
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """
        Test for reload method
        """
        self.storage.reload()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(self.storage._FileStorage__objects, {})

if __name__ == "__main__":
    unittest.main()
