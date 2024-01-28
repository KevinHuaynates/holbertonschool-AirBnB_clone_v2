#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """This class defines the attributes of DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """This is the init method for DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB'),
                                              pool_pre_ping=True))

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This returns a dictionary of models currently in storage"""
        result = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = []
            for c in BaseModel.__subclasses__():
                objs += self.__session.query(c).all()
        for obj in objs:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            result[key] = obj
        return result

    def new(self, obj):
        """This adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """This saves all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """This deletes the given object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """This creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call remove() method on the private session attribute (self.__session)"""
        self.__session.remove()
