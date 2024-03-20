#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    if models.storage_source == "db":
        __tablename__ = "reviews"

        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        place = relationship("Place", back_populates="reviews")
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        user = relationship("User", back_populates="reviews", cascade=("all, delete"))
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """Initializes the review"""
        super().__init__(*args, **kwargs)
