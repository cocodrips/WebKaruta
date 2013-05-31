#!-*- coding:utf-8 -*-"

import flask as f
import bp

app = f.Flask(__name__)


@app.route('/')
def index():
    return f.redirect('/vis')


@app.route('/vis', methods=['POST', 'GET'])
def vis_index():
    if f.request.method == "GET":
        data = bp.Karuta.json_data()
        return f.render_template("visualization.html", word="", data=data, apiData="", keyword="", maching="")
    else:
        word = f.request.form['word']
        query_num = f.request.form['query_num']
        return f.redirect('/vis/' + word + '/' + query_num)


@app.route('/vis/<word>/<query_num>', methods=['POST', 'GET'])
def vis(word, query_num):
    analyze = bp.Analyze.create(word, query_num)
#    data = bp.Karuta.json_data()
    return f.render_template("visualization.html", word=word, links=analyze.links, titles=analyze.titles, keyword=analyze.summary_hash_top, matching=analyze.matching_array)


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


if __name__ == '__main__':
    print app.has_static_folder
    app.debug = True
    app.run()