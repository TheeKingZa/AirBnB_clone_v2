#!/usr/bin/python3
"""
Module for FileStorage class
"""

import json
import os

class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the dictionary __objects
        """
        if cls is not None:
            filtered_objects = {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
            return filtered_objects
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the file exists)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value["__class__"]
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it's inside
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()
