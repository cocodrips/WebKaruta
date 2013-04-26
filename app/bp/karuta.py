#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
from google.appengine.ext import db
from bp.base import Progress, Ingredient, Listable
from bp.source import Source

class Karuta(db.Model):
    """
    Entree is a item which belongs a Plate.
    Entree is a view of Source in the specific plate.

    Entree has a Plate as its parent.
    """
    created_at = db.DateTimeProperty(auto_now_add = True)
    updated_at = db.DateTimeProperty(auto_now = True)
    source = db.ReferenceProperty(reference_class = Source, required = True)
    # ... Denoralized source detai will come here ...

    @property
    def title(self):
        return self.source.title

    @property
    def review(self):
        return self.source.review

    @property
    def who_reviewed(self):
        return self.source.who_reviewed

    @property
    def cqflag(self):
        return self.source.cqflag

    @property
    def modified_at(self):
        return self.source.modified_at

    @property
    def status(self):
        return self.source.status

    @property
    def view_url(self):
        return "/e/" + str(self.key())


    @classmethod
    def json_data(cls):

        f = open("static/matrixEn.json")
        data = json.load(f)
        return data

    @classmethod
    def create(cls, plate, source_url):
        source = Source.ensure_by_url(source_url)
        found = cls.all().ancestor(plate).filter('source = ', source).get()
        if found:
            raise ValueError, "found"
        return 0
#        fresh = cls(paren
#            found = cls.all().ancestor(plate).filter('source = ', source).get()
#            return found

    @classmethod
    def delete_by_key(cls, key):
        entree = cls.find_by_key(key)
        if entree:
            entree.delete()
            return None
        return None

    @classmethod
    def list_by_plate(cls, plate, limit=100):
        return cls.all().ancestor(plate).fetch(limit=limit)

    @classmethod
    def list_by_source(cls, source, limit=100):
        return cls.all().filter('source =', source).fetch(limit=limit)

    @classmethod
    def find_by_key(cls, key):
        return cls.get(key)
