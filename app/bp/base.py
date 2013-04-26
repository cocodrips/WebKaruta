
import urllib

class Enum(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return name


class Progress(object):
    REPORTED = Enum(0, "CREAED")
    STARTED  = Enum(1, "STARTED")
    CLOSED   = Enum(2, "CLOSED")


class Ingredient(object):
    def __init__(self):
        self.opened_at = None
        self.closed_at = None
        self.title = None
        self.progress  = Progress.REPORTED
        self.bag = {}


class Listable(object):
    @classmethod
    def list(cls, limit=100):
        return cls.all().fetch(limit = limit)


urlopen = urllib.urlopen
