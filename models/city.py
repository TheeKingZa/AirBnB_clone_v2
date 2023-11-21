#!/usr/bin/python3
""" City Module for HBNB project """
# Import the necessary modules
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """The city class, contains state ID and name"""
    if models.storage_type == 'db':
        # Define the table name for SQLAlchemy
        __tablename__ = 'cities'
        # Define columns for SQLAlchemy
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
