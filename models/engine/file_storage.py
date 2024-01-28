#!/usr/bin/python3
"""This module defines a class to manage file storage for HBNB"""
import json
import models


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        save_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(save_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                loaded_dict = json.load(f)
            for key, val in loaded_dict.items():
                class_name = val['__class__']
                new_obj = models.classes[class_name](**val)
                FileStorage.__objects[key] = new_obj
        except FileNotFoundError:
            pass


    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()
