#!/usr/bin/python3
"""
This module contains the definition of the User class
that inherits BaseModel.
"""
from .base_model import BaseModel


class User(BaseModel):
    """

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""