#!/usr/bin/python
""" Class Amenity """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Child Class of BaseModel Class """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
