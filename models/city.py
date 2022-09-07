#!/usr/bin/python
""" Class City """
from models.base_model import BaseModel


class City(BaseModel):
    """ Child Class of BaseModel Class """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
