#!-*- coding:utf-8 -*-"
import sys
sys.path.append("third_party/Flask-0.9/")
sys.path.append("third_party/Werkzeug-0.8.3/")
sys.path.append("third_party/python-dateutil-2.1/")
sys.path.append("third_party/six-1.1.0/")
sys.path.append("third_party/beautifulsoup4-4.1.1/")

import flask as f
import bp


app = f.Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    return f.redirect('/p')


@app.route('/p', methods=['POST', 'GET'])
def plate_index():
    if f.request.method == "GET":
        data = bp.Karuta.json_data()
        return f.render_template("karuta_index.html",word="", data=data)
    elif f.request.method == "POST":
        # user = bp.User.ensure(users.get_current_user())
        try:
            word = f.request.form['word']
            # created = bp.Plate.create(user, f.request.form['name'])
            return f.redirect('/p/' + word)
        except ValueError:
            err = 'Conflicting name'
            f.flash(err)
            return f.redirect(f.request.referrer)
    else:
        raise Exception("Hello")


@app.route('/p/<word>', methods=['POST', 'GET'])
def plate(word):
    data = bp.Karuta.json_data()
    return f.render_template("karuta_index.html", word=word, data=data)

@app.route('/k', methods=['POST', 'GET'])
def k():
	return "k"




#
#
#
# @app.route('/p/<name>/more', methods=['POST'])
# def plate_add_bug(name):
#     plate = bp.Plate.find_by_name(name)
#     match = re.match("https://bugs.webkit.org/show_bug.cgi\\?id=[0-9]*", f.request.form["url"])
#     if match == None:
#         err = 'You should input bug url'
#         f.flash(err)
#         return f.redirect(plate.view_url)
#     try:
#         bp.Entree.create(plate, match.group())
#     except ValueError:
#         err = 'Entree has already this url'
#         f.flash(err)
#     return f.redirect(plate.view_url)
#
#
# @app.route('/p/<name>/delete', methods=['POST'])
# def plate_delete(name):
#     try:
#         bp.Plate.delete_by_name(name)
#         return f.redirect('/p')
#     except ValueError:
#         err = 'You can\'t delete this plate'
#         f.flash(err)
#         return f.redirect(f.request.referrer)
#
# @app.route('/p/<name>/edit', methods=['POST'])
# def plate_edit(name):
#     plate = bp.Plate.find_by_name(name)
#     try:
#         plate.edit_name(f.request.form["rename"])
#         return f.redirect('/p/' + f.request.form["rename"])
#     except ValueError:
#         err = 'Failed rename'
#         f.flash(err)
#         return f.redirect(f.request.referrer)
#
#
# @app.route('/add/<path:url>', methods=['GET'])
# def add_source(url):
#     match = re.match("https://bugs.webkit.org/show_bug.cgi\?id=", url)
#     if match:
#         return f.render_template("add_bug.html", plates=bp.Plate.list(), source_url=urllib.quote_plus(url), source_url_decoded=url)
#     else:
#         return f.redirect(f.request.referrer)
#
#
# @app.route('/add/<path:url>/refresh', methods=['POST'])
# def add_source_and_refresh(url):
#     bp.Plate.refresh_source(url, f.request.form['name'])
#     return f.redirect('/p/' + f.request.form['name'])
#
#
# @app.route('/e/<key>/delete', methods=['POST'])
# def entree_delete(key):
#     bp.Entree.delete_by_key(key)
#     return f.redirect(f.request.referrer)
#
#
# @app.route('/s', methods=['GET'])
# def source_index():
#     return f.render_template("source_index.html", sources=bp.Source.list())
#
#
# @app.route('/s/<path:url>', methods=['GET'])
# def source(url):
#     source = bp.Source.find_by_url(url)
#     return f.render_template("source.html", source=source, plates=source.plates)
#
#
# @app.route('/s/<path:url>/refresh', methods=['POST'])
# def source_refresh(url):
#     source = bp.Source.find_by_url(url)
#     if not source:
#         return f.redirect(f.request.referrer)
#     source.refresh()
#     source.put()
#     return f.redirect(f.request.referrer)
