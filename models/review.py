#!/usr/bin/python3
"""Base Model Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The Review class"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """review init"""
        super().__init__(*args, **kwargs)

