#!/usr/bin/python
""" Class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Child Class of BaseModel Class """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)