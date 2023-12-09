#!/usr/bin/python3
"""BaseMODEL CLASS"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Amenity init"""
        super().__init__(*args, **kwargs)
