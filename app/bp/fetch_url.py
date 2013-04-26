
from xml.etree.ElementTree import ElementTree
import StringIO
import bp
import datetime
import dateutil.parser
import re
from bs4 import BeautifulSoup

def make_extractor_from(url):
    if 0 == url.find("https://bugs.webkit.org/show_bug.cgi?"):
        return BugzillaExtractor(url)
    raise Exception("Unkwown URL")


class BugzillaExtractor(object):
    def __init__(self, source_url):
        self.source_url = source_url

    @property
    def fetching_urls(self):
        bugid = re.search("\d+", self.source_url).group(0)
        return { "bug": self.source_url + "&ctype=xml", 
                 "activity": "https://bugs.webkit.org/show_activity.cgi?id=" + bugid }
    
    def extract(self, dataset):
        tree = ElementTree(file=StringIO.StringIO(dataset["bug"]))
        soup = BeautifulSoup(dataset["activity"])
        result = bp.Ingredient()
        result.title = self._extract_title(tree)
        result.created_at = self._extract_created_at(tree)
        result.closed_at = self._extract_closed_at(soup)
        return result

    def _extract_title(self, tree):
        return tree.findtext(".//short_desc")

    def _extract_created_at(self, tree):
        return dateutil.parser.parse(tree.findtext(".//creation_ts"))

    def _extract_closed_at(self, soup):
        def strip(str_or_null):
            if str_or_null:
                return str_or_null.strip()
            else:
                return ""

        table = soup.find_all("table")[1]
        
        for tr in table.find_all("tr", recursive=False)[1:]:
            tds = [strip(t.string) for t in tr.find_all("td")]

            
            if len(tds) < 5:
                next 
            # print "[", tds, "]"

            if len(tds) == 5:
                who, when, what, removed, added = tds
            elif len(tds) == 3:
                what, removed, added = tds
            if re.search("FIXED", added):
                return dateutil.parser.parse(when)
        return None

class Fetcher(object):
    def __init__(self, url):
        pass

    def run(self):
        # normalize URL
        # fetch
        # extract summary
        # store summary
        pass
