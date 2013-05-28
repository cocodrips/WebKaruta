#!-*- coding:utf-8 -*-"
import sys
sys.path.append("third_party/Flask-0.9/")
sys.path.append("third_party/Werkzeug-0.8.3/")
sys.path.append("third_party/python-dateutil-2.1/")
sys.path.append("third_party/six-1.1.0/")
sys.path.append("third_party/beautifulsoup4-4.1.1/")
sys.path.append("third_party/html5lib-python-master/")

import  logging
import flask as f
from flask import jsonify
import bp

app = f.Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    return f.redirect('/vis')


@app.route('/vis', methods=['POST', 'GET'])
def vis_index():
    if f.request.method == "GET":
        data = bp.Karuta.json_data()
        return f.render_template("visualization.html",word="", data=data, apiData="", keyword="", maching="")
    else:
        word = f.request.form['word']
        query_num = f.request.form['query_num']
        return f.redirect('/vis/' + word + '/' + query_num)


@app.route('/vis/<word>/<query_num>', methods=['POST', 'GET'])
def vis(word, query_num):
    analyze = bp.Analyze.create(word, query_num)
#    data = bp.Karuta.json_data()
    return f.render_template("visualization.html", word=word, links=analyze.links, titles=analyze.titles, keyword=analyze.summary_hash, matching=analyze.matching_array)



@app.route('/k', methods=['POST', 'GET'])
def k():
	return "k"


@app.route('/d3', methods=['POST', 'GET'])
def d3():
    data = bp.Karuta.json_data()
    return f.render_template("test.html", data=data)


@app.route('/treemap', methods=['POST', 'GET'])
def treemap():
#    data = bp.Karuta.json_data()
    return f.render_template("treemap.html")


