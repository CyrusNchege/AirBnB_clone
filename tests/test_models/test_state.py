#!/usr/bim/python3
"""Unittest for State class"""
import unittest
from models.state import State
from models.base_model import BaseModel
import datetime


class TestState(unittest.TestCase):
    """
        Test cases for State class
    """
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def test_init(self):
        """
            Test for __init__ method
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at)
        self.assertIsInstance(state.updated_at)

    def test_state_is_subclass(self):
        """
            Test if State is subclass of BaseModel
        """
        state = State()
        self.assertTrue(issubclass(state.__class__, BaseModel), True)

    def test_name_attr(self):
        """
            Test for name attribute
        """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_two_models_unique_ids(self):
        """
            Test for unique id
        """
        state = State()
        state1 = State()
        self.assertNotEqual(state.id, state1.id)

    def test_str(self):
        """
            Test for __str__ method
        """
        state = State()
        string = "[{}] ({}) {}".format(state.__class__.__name__, state.id,
                                       state.__dict__)
        self.assertEqual(string, str(state))

    def test_to_dict(self):
        """
            Test for to_dict method
        """
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)
        self.assertEqual(state_dict['__class__'], 'State')

    def test_save(self):
        """
            Test for save method
        """
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

if __name__ == "__main__":
    unittest.main()
