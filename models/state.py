#!/usr/bin/python3
""" State Module for HBNB project """
# Import the necessary modules
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """State class"""
    if models.storage_type == 'db':
        # Define the table name for SQLAlchemy
        __tablename__ = 'states'
        # Define columns for SQLAlchemy
        name = Column(String(128), nullable=False)
        # Relationship with City (for DBStorage)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        # Getter attribute for FileStorage
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances
               with state_id equals to the current State.id
            """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
