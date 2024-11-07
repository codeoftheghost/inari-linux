#!/usr/bin/python3

"""
Copyright (c) 2006-2024 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from plugins.generic.takeover import Takeover as GenericTakeover

class Takeover(GenericTakeover):
    def __init__(self):
        self.__basedir = None
        self.__datadir = None

        GenericTakeover.__init__(self)
