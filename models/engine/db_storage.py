#!/usr/bin/python3

"""
New Engine
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import sqlalchemy
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "City": City, "Place": Place, 
"Review": Review, "State": State, "User": User}

class DBStorage():

    __engine = None
    __session = None

    def __init__(self, *args, **kwargs):
        """ Creates the engine """
        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
        format(username, password, host, database), 
        pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session """
        new_dict = {}

        if cls is None:
            for classType in classes:
                objects = self.__session.query(classes[classType]).all()

                for obj in objects:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj

        else:
            if cls in classes:
                objects = self.__session.query(classes[cls]).all()
                for obj in objects:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj

        return new_dict

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes from the current database """

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database """

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)