#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage
   based on the value of the environment variable HBNB_TYPE_STORAGE
"""

from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Select storage type based on the environment variable HBNB_TYPE_STORAGE
storage_type = getenv('HBNB_TYPE_STORAGE')

# If HBNB_TYPE_STORAGE is set to 'db', use DBStorage
if storage_type == 'db':
    storage = DBStorage()

# If HBNB_TYPE_STORAGE is not set or set to anything other than 'db', use FileStorage
else:
    storage = FileStorage()

# Load data from storage
storage.reload()
