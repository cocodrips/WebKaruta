from xml.etree.ElementTree import ElementTree
import StringIO

import sys
import datetime
import urllib
import logging
import re
import dateutil.parser

from google.appengine.ext import db
from bp.base import Progress, Ingredient, Listable
import dateutil.parser



class Analyze(db.Model):
    keyword = db.TextProperty(required=True)
    title = db.TextProperty()
    title_word = db.TextProperty()
    abstract = db.TextProperty()
    url = open('/Users/Chiichan/Documents/python/WebKaruta/tests/data/result.xml', 'r')
    tree = ElementTree(file=StringIO.StringIO(url))


    @classmethod
    def create(cls, keyword):
	    return "Yahoo!"
	    pass
        # found = cls.all().ancestor(plate).filter('source = ', source).get()
        # if found:
        #     raise ValueError, "found"
        # return 0
#        fresh = cls(paren
#            found = cls.all().ancestor(plate).filter('source = ', source).get()
#            return found
    def extract(cls, keyword):

        return "Yahoo!"
        pass

    def _extract_title(self, soup):

        return "Yahoo!"
        pass
    @classmethod
    def delete_by_keyword(cls, key):
		pass
        # entree = cls.find_by_key(key)
        # if entree:
        #     entree.delete()
        #     return None
        # return None

    @classmethod
    def find_by_keyword(cls, key):
	    pass
        # return cls.get(key)
