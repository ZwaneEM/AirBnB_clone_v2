#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.amenity import Amenity, place_amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_source == "db":
        __tablename__ = "places"

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        cities = relationship("City", back_populates="places")
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        user = relationship("User", back_populates="places")
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship("Review", back_populates="place", cascade=("all, delete"))
        amenities = relationship("Amenity", 
                                 secondary=place_amenity,
                                 viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ Initializes teh Place """
        super().__init__(*args, **kwargs)

    if models.storage_source != "db":
        @property
        def reviews(self):
            review_dict = models.storage.all("Review")
            filtered_list = []
            for value in review_dict.values():
                if value.place_id == self.id:
                    filtered_list.append(value)

            return filtered_list
        
        @property
        def amenities(self):
            """ Return the list of Amenity instances """
            amenity_list = []

            all_amenities = models.storage.all("Amenity")
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list
    
        