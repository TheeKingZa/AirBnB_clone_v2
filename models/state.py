#!/usr/bin/python3
""" State Module for HBNB project """
# Import the necessary modules
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """State class"""
    if models.storage_type == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
        
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
            cities_list = []
            if models.storage_type == 'db':
                for city in self.cities:
                    cities_list.append(city)
            else:
                for city_id, city in models.storage.all(City).items():
                    if city.state_id == self.id:
                        cities_list.append(city)
            return cities_list
