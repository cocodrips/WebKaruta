# coding: UTF-8
import xml.etree.ElementTree as ElementTree
from bs4 import BeautifulSoup
import html5lib
from html5lib import treebuilders
from html5lib import serializer
import sys

import urllib
import urllib2
import logging
import re
from google.appengine.ext import db
import bp


class Analyze():
    query_num = 1
    links = []
    titles = []
    summaries = []
    matching_array = []

    def __init__(self, keyword, query_num):
        self.query_num = query_num
        self.extract(keyword)
        self.compare_urls()

    @property
    def key_hash(self):
        return self.count_keyword(self.titles)

    @property
    def summary_hash(self):
        return self.count_keyword(self.summaries)

    def extract(self, keyword):
        appId = "83dpVeexg66u4NJrtfaO.vwNqPZTZw266pNUlLoi76oId_2S2ob.k7ygCoT0YJRdwg--"
        apiUrl = "http://search.yahooapis.jp/WebSearchServicePro/V1/webSearch?"
        yahooTag = "{urn:yahoo:jp:srch}"
        params = urllib.urlencode(
            {'appid': appId,
             'query': keyword,
             'results': self.query_num,
             'language':"en",
            })

        logging.info("_______Access_______")
        logging.info(apiUrl+params)

        response = urllib.urlopen(apiUrl+params).read()
        tree = ElementTree.fromstring(response)

        for url in tree.getiterator(yahooTag+"ClickUrl"):
            data = {}
            data["url"] = url.text

            urls = self.extract_links(str(url.text))
            if urls == "error":
                data["childUrl"] = []
            else:
                data["childUrl"] = urls
            self.links.append(data)

        for title in tree.getiterator(yahooTag+"Title"):
            self.titles.append(title.text)
        for summary in tree.getiterator(yahooTag+"Summary"):
            self.summaries.append(summary.text)

    def extract_links(self, url):
        urls = []
        logging.info("_______Analyze_______")
        logging.error(url)

        try:
            html = urllib2.urlopen(url)
        except urllib2.URLError, e:
            if e.code >= 400:
                return "error"
            else:
                return "error"

        soup = BeautifulSoup(html, "html5lib")
        html_pattern = re.compile(r'(http://[A-Za-z0-9\'~+\-=_.,/%\?!;:@#\*&\(\)]+)')
        try:
            for _a in soup.findAll('a'):
                href = _a.get('href')
                if href != None:
                    m = html_pattern.match(str(href.encode('utf_8')))
                    if m != None:
                        urls.append(href)
        except ValueError:
            return "error"
        return urls

    def compare_urls(self):
        self.query_num = int(self.query_num)
        self.matching_array =  [[False for j in range(self.query_num)] for i in range(self.query_num)]
        for i in range(self.query_num):
            for j in range(self.query_num):
                if i == j :
                    self.matching_array[i][j] = False
                else:
                    self.matching_array[i][j] = self.matching_urls(self.links[i], self.links[j])
        logging.info("_______Compare_result_______")
        logging.error(self.matching_array)


    def matching_urls(self, urls1, urls2):
        logging.info("_______links_______")
        logging.error(urls1["childUrl"])
        for src in urls1["childUrl"]:
            for target in urls2["childUrl"]:
                if src == target:
                    return True
        return False


    def count_keyword(self, target):
        hash = {}
        for p in target:
            keys = p.split(' ')
            for key in keys:
                if key in hash:
                    hash[key] = hash[key] + 1
                else:
                    hash[key] = 1
        hash = sorted(hash.items(), key=lambda x:x[1], reverse=True)
        return hash


    @classmethod
    def create(cls, keyword, query_num):
        analyze = Analyze(keyword, query_num)
        return analyze

