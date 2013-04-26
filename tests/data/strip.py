# -*- coding:utf-8 -*-

import re
import urllib
import sys
import time
import xml.dom.minidom

f = file('result.xml', 'a')

appid = "dj0zaiZpPVNpT0xsWGc3ajEwVSZkPVlXazlTVm8zWVZsNk5Xa21jR285TUEtLSZzPWNvbnN1bWVyc2VjcmV0Jng9MjI-"
secret = "3ed6b1d59dceb918baf3bb280a58c411dabe9e89"
query = "default"

url = "http://search.yahooapis.jp/WebSearchService/V2/webSearch"

for x in xrange(2,20):
    params = {
    "appid" : appid,
    "query" : query,
    "start" : x
    }

    params = urllib.urlencode(params)
    print url + '?' + params


    for _ in range(100):
        response = urllib.urlopen(url + '?' + params)
        results = response.read()
        
        dom = xml.dom.minidom.parseString(results)
        error = dom.getElementsByTagName("Error")
        if len(error) > 0 :
            msg = error[0].firstChild.firstChild.data
            sys.stderr.write("[Error] {0}\n".format(msg))
            time.sleep(2)
            continue
        
        print "Successfully get data."
        print results
        f.write("----------------" + str(x) + "----------------\n")
        f.write(results)
        break


def getText(node):
    for n in node.childNodes:
        if n.nodeType in [node.TEXT_NODE, node.COMMENT_NODE]:
            return n.data
        else:
            return ''

# requesturl = url(appid, query)
# response = urllib.urlopen(requesturl).read()

# doc = xml.dom.minidom.parseString(response)

# text = u"Web検索結果のクラスタ分布の可視化の一手法"
# text_en = " I am Chica."
# r = re.compile(r'\s')
# split = re.split('[A-z]',text)

# if split:
#     for s in split:
#         print s.encode('utf-8')
# else:
#     print "not match"


