#!/usr/bin/python3
"""Base Model class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State Class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """State init"""
        super().__init__(*args, **kwargs)

