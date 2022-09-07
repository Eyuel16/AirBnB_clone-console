#!/usr/bin/python
""" Class State """
from models.base_model import BaseModel


class State(BaseModel):
    """ Child Class of BaseModel Class """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
