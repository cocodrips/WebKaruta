import unittest
import os
import datetime
import helpers
import bp
import re
import logging

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

class AnalyzeTest(unittest.TestCase, helpers.DataStoreTestHelper):

    def setUp(self):
        self.setUpBed()
        self.target_url = open(os.path.join(DATA_DIR,"results.xml"),'r')

    def tearDown(self):
        self.tearDownBed()

    def test_create(self):
        soup = bp.Analyze.create("AnalyzeTest")
        logging.info(soup);


    def test_title(self):
        soup = bp.Analyze.create("AnalyzeTest")

#        self.assertEquals(self.target.source_url,self.target_url)

#    def test_title(self):
#        self.target.source.refresh()
#        self.assertEquals(self.target.title,"[Refactoring] Replace Node's Document pointer with a TreeScope pointer")
#
#    def test_view_url(self):
#        self.assertTrue(re.match("/e/",self.target.view_url))
#
#    def test_find_by_key(self):
#        found = bp.Entree.find_by_key(self.target.key())
#        self.assertEquals(self.target.source_url, found.source_url)
#
#    # def test_find_by_source_url_and_plate_name(self):
#    #     found = bp.Entree.find_by_source_url_and_plate_name(self.source, self.plate)
#    #     self.assertEquals(found.source_url,self.target_url)
#
#    def test_ensure_by_url_with_entree(self):
#        target = bp.Entree.ensure_by_url(self.plate, self.target_url)
#        self.assertEquals(target.source_url,self.target.source_url)
#
#    def test_ensure_by_url_without_entree(self):
#        target_url = "https://bugs.webkit.org/show_bug.cgi?id=61801"
#        target = bp.Entree.ensure_by_url(self.plate, target_url)
#        self.assertEquals(target.source_url,target_url)
