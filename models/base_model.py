#!/usr/bin/python3
"""
Contains class BaseModel
"""
from datetime import datetime
import models
import uuid
time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time_format)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """String representation of BaseModel object"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id,
                                         self.__dict__)

    def save(self):
        """Saves objects to a Json file. Updated_at attribute
        will be updated with the time the object is saved to the file.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all attributes
        of an object with the respective values.
        """
        dictionary = self.__dict__.copy()
        if "created_at" in dictionary.keys():
            dictionary["created_at"] = dictionary["created_at"].strftime(time_format)
        if "updated_at" in dictionary.keys():
            dictionary["updated_at"] = dictionary["updated_at"].strftime(time_format)
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

