#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if models.storage_source == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        Cities = relationship("City", backref="states")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ initializing state """
        super().__init__(*args, **kwargs)

    if models.storage_source != 'db':
        @property
        def cities(self):
            """ Getter attribute for cities """
            from models import storage
            city_instances = storage.all(City)
            cityList = []

            for city in city_instances.values():
                if city.state_id == self.id:
                    cityList.append(city)
            return cityList
