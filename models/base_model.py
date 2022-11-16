#!/usr/bin/python3
"""
This module defines BaseModel - a base class for all
AIRBNB project objects
"""
from uuid import uuid4
from datetime import datetime


datetime_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Definition of the BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel object
        """
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], datetime_format)
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], datetime_format)

            del kwargs['__class__']
            self.__dict__.update(kwargs)
        else:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns string representation of the BaseModel object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Method that sets the time object was updated
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Generates a dictionary representation of the object
        """
        dic = {}
        dic.update(self.__dict__)
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic