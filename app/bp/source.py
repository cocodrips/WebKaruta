import datetime
import urllib
import logging
import bp.base
import bp.fetch

class Source(db.Model, bp.base.Listable):
    """
    Source captures a tracked web page which contains the canonical information of the entree.
    It is typically a Bugzilla page.
    """
    created_at = db.DateTimeProperty(auto_now_add = True)
    updated_at = db.DateTimeProperty(auto_now = True)
    url = db.LinkProperty(required = True)
    title = db.StringProperty()
    review = db.StringProperty()
    who_reviewed = db.StringProperty()
    cqflag = db.StringProperty()
    modified_at = db.DateTimeProperty()
    status = db.StringProperty()

    @property
    def view_url(self):
        return "/s/" + urllib.quote_plus(self.url)

    @property
    def entrees(self):
        return self.__class__.entree_class.list_by_source(self)

    @property
    def plates(self):
        return [ e.plate for e in self.entrees ]

    def fetch_ingredient(self):
        extractor = bp.fetch.make_extractor_from(self.url)
        fetching_urls = extractor.fetching_urls
        bug_data = bp.base.urlopen(fetching_urls["bug"]).read()
        activity_data = bp.base.urlopen(fetching_urls["activity"]).read()
        ingredient = extractor.extract({ "bug": bug_data, "activity": activity_data })
        return ingredient

    def set_ingredient(self, ingredient):
        self.title = ingredient.title
        self.review = ingredient.review
        self.who_reviewed = ingredient.who_reviewed
        self.cqflag = ingredient.cqflag
        self.modified_at = ingredient.modified_at
        self.status = ingredient.status

    def refresh(self):
        """
        Fetches and extracts the url content and
        save myself.
        """
        self.set_ingredient(self.fetch_ingredient())


    @classmethod
    def ensure_by_url(cls, url):
        found = cls.find_by_url(url)
        if found:
            return found
        fresh = cls(url = db.Link(url))
        fresh.put()
        return fresh

    @classmethod
    def find_by_url(cls, url):
        return cls.all().filter('url = ', db.Link(url)).get()

