#!/usr/bin/python3
"""
    contains the class Review
"""
from models.base_model import BaseModel
from models.base_model import Review
import unittest
import datetime


class TestReview(unittest.TestCase):
    """
    class TestReview
    """

    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def test_init(self):
        """
        test for init
        """
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime.datetime)
        self.assertIsInstance(review.updated_at, datetime.datetime)

    def test_review_is_subclass(self):
        """
        test for review is subclass
        """
        review = Review()
        self.assertTrue(issubclass(review.__class__, BaseModel), True)

    def test_place_id_attr(self):
        """
        test for place id attr
        """
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_user_id_attr(self):
        """
        test for user id attr
        """
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
    
    def test_text_attr(self):
        """
        test for text attr
        """
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

if __name__ == '__main__':
    unittest.main()
