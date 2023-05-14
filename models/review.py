#!/usr/bin/python3
"""
    model for review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Class Review inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
