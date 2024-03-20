#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Table

place_amenity = Table('association', Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Amenity(BaseModel, Base):
    """Hbnb Amenities"""

    if models.storage_source == "db":
        __tablename__ = "amenities"

        name = Column(String(128), nullable=False)

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes the amenity class """
        super().__init__(*args, **kwargs)
