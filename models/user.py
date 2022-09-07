#!/usr/bin/python
""" Class User """
from models.base_model import BaseModel


class User(BaseModel):
    """ Child Class of BaseModel Class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)