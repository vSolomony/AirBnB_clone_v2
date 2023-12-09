#!/usr/bin/python3
"""Basemodel Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """city init"""
        super().__init__(*args, **kwargs)

