#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
from bp.base import Progress, Ingredient, Listable

class Karuta():

    @classmethod
    def json_data(cls):
        f = open("static/matrixEn.json")
        data = json.load(f)
        return data

