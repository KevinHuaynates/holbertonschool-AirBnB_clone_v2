# models/state.py
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

    else:
        @property
        def cities(self):
            """Returns the list of City objects linked to the current State"""
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
