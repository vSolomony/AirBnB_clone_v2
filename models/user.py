#!/usr/bin/python3
"""Base model class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """The class User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

