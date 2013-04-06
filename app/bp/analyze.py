from xml.etree.ElementTree import ElementTree
import StringIO

import sys
import datetime
import urllib
import logging
import re
import dateutil.parser

from google.appengine.ext import db
import bp
import dateutil.parser



class Analyze():
    url = ""
    def __init__(self, url):
        logging.info("___init__")
        result = self.extract(keyword)
        return result

    def extract(self, keyword):
        result = bp.Ingredient()
        url = urllib.urlopen('http://feeds.feedburner.com/GoogleJapanBlog')
        tree = ElementTree(file=url)
        title = self._extract_title(tree)
        logging.info("__"+ title +"__")
        return title

    def _extract_title(self, tree):
        return "chii"


    @classmethod
    def create(cls, keyword):
	    pass
        # found = cls.all().ancestor(plate).filter('source = ', source).get()
        # if found:
        #     raise ValueError, "found"
        # return 0
#        fresh = cls(paren
#            found = cls.all().ancestor(plate).filter('source = ', source).get()
#            return found


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
