#!/usr/bin/python3
"""base model module"""


import uuid
from datetime import datetime
import json


class BaseModel:
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialization method for BaseModel"""
        if kwargs:
            # If kwargs is provided, set attributes based on its values
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            # Convert created_at and updated_at strings to datetime objects
            self.created_at = datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            self.updated_at = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
        else:
            # If no kwargs, set new id, created_at, and updated_at
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """String representation of BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert the BaseModel instance to a dictionary"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

