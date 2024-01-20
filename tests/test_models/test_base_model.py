#!/usr/bin/python3
"""Tests for BaseModel class"""
from models.base_model import BaseModel
import unittest
import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def tearDown(self):
        """Remove the file.json after each test"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """Test creating an instance with default values"""
        i = BaseModel()
        self.assertEqual(type(i), BaseModel)

    def test_kwargs(self):
        """Test creating an instance with kwargs"""
        i = BaseModel()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test creating an instance with kwargs containing int"""
        i = BaseModel()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test save method"""
        i = BaseModel()
        i.save()
        key = "BaseModel." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test __str__ method"""
        i = BaseModel()
        self.assertEqual(str(i), '[BaseModel] ({}) {}'.format(i.id, i.__dict__))

    def test_todict(self):
        """Test to_dict method"""
        i = BaseModel()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test creating an instance with kwargs containing None"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_kwargs_one(self):
        """Test creating an instance with kwargs containing one key"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = BaseModel(**n)

    def test_id(self):
        """Test id attribute"""
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test created_at attribute"""
        new = BaseModel()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

if __name__ == '__main__':
    unittest.main()

