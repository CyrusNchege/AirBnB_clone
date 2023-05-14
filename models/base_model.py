#!/usr/bin/python3
"""
A model to implement a BaseModel class
"""

from uuid import uuid4
from datetime import datetime   


class BaseModel:
    """
    BaseModel class for all other classes

    Attributes:
        id (str): unique id for each instance
        created_at (datetime): time of creation
        updated_at (datetime): time of update
    """

    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance

        Args:
            args (tuple): unused
            kwargs (dict): key/value pairs of attributes
        """
        from models import storage
        if not kwargs:
            self.id = BaseModel.id
            self.created_at = BaseModel.created_at
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)


    def __str__(self):
        """
        Returns a string representation of the instance
        """  
        return "[{}] ({}) {}".format(
            self.__class__.__name__, 
            self.id, 
            self.__dict__
            )
    
    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
