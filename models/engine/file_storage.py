#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            # If cls is provided, filter objects based on the class
            return {k: v for k, v in FileStorage.__objects.items() if isinstance(v, cls)}
        # If cls is not provided, return all objects
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        # Create a key using the class name and object id
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        # Add the object to the storage dictionary
        self.all().update({key: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            # Convert objects to their dictionary representation before saving
            for key, val in temp.items():
                temp[key] = val.to_dict()
            # Save the dictionary to the file in JSON format
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        # Mapping of class names to their corresponding classes
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                # Load the data from the file
                temp = json.load(f)
                # Create objects from the loaded data and add them to the storage dictionary
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            # If the file does not exist, do nothing
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj is not None:
            # Create the key using the class name and object id
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            # Check if the key exists in the storage dictionary
            if key in self.all():
                # If it exists, delete the key and save the updated dictionary
                del self.all()[key]
                self.save()
    
    def close(self):
        """
        Close the file and call reload()
        For deserializing the JSON file to objects.
        """
        self.reload()        
