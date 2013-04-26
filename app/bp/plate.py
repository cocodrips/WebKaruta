import datetime
import urllib
import bp
import dateutil.parser
import flask as f

from google.appengine.ext import db
from google.appengine.api import users

from bp.base import Progress, Ingredient, Listable
from bp.entree import Entree


class User(db.Model):
    account = db.UserProperty()

    @classmethod
    def ensure(cls, api_user):
        found = cls.all().filter('account = ', api_user).get()
        if found:
            return found
        fresh = cls(account=api_user)
        fresh.put()
        return fresh


class Plate(db.Model, Listable):
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)
    name = db.StringProperty(required=True)
    owner = db.ReferenceProperty(reference_class=User)

    @property
    def owner_email(self):
        return self.owner.account.email()

    @property
    def view_url(self):
        return "/p/" + urllib.quote_plus(self.name)

    @property
    def entrees(self):
        return Entree.list_by_plate(self)

    @property
    def entrees_ordered(self):
        return self.entrees_ordered_by_status(self.entrees_ordered_by_modified_at(self.entrees))

    def entrees_ordered_by_modified_at(self, entrees):
        def entrees_date(entrees):
            if not entrees.modified_at:
                return datetime.datetime(1, 1, 1, 0, 0, 0)
            return entrees.modified_at
        return sorted(entrees, key=entrees_date, reverse=True)

    def entrees_ordered_by_status(self, entrees):
        return sorted(entrees, None, Plate.entrees_status)

    @classmethod
    def entrees_status(cls, entrees):
        status_num = {
            "review?": 0,
            "review-": 1,
            "review+": 2,
            "RESOLVED": 4,
        }
        if not entrees.status:
            return 3
        elif entrees.status == "RESOLVED":
            return status_num[entrees.status]
        elif not entrees.review:
            return 3
        else:
            return status_num[entrees.review]

    def edit_name(self, rename):
        user = users.get_current_user()
        if self.owner.account != user:
            raise ValueError, "You aren't owner"
        if Plate.find_by_name(rename) or rename == "":
            raise ValueError, "Value error"
        self.name = rename
        self.put()

    @classmethod
    def create(cls, owner, name):
        if name == "":
            raise ValueError, "empty"
        found = cls.find_by_name(name)
        if found:
            raise ValueError, "found"
        fresh = cls(owner=owner, name=name)
        fresh.put()
        return fresh

    @classmethod
    def delete_by_name(cls, name):
        user = users.get_current_user()
        found = cls.find_by_name(name)
        if found.owner.account != user:
            raise ValueError, "You aren't owner"
        if not found:
            raise ValueError, "found"
        found.delete()

    @classmethod
    def find_by_name(cls, name):
        return cls.all().filter('name = ', name).get()

    @classmethod
    def find_plate_list(cls):
        return cls.all().fetch(limit=100)

    @classmethod
    def find_by_owner(cls, owner):
        return cls.all().filter('owner = ', owner).fetch(limit=100)

    @classmethod
    def refresh_source(cls, source_url, plate_name):
        plate = cls.find_by_name(plate_name)
        bp.Entree.ensure_by_url(plate, source_url)
        source = bp.Source.find_by_url(source_url)
        source.refresh()
        source.put()