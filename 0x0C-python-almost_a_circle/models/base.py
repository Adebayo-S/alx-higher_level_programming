#!/usr/bin/python3
"""
class Base: is the base for all other classes in this project
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id, increment class attribute if no id
        and set as id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
