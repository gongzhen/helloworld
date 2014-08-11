from flask import Flask, request, render_template, redirect, url_for, request
# from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
# bootstrap = Bootstrap()
# bootstrap.init_app(app)

# http://stackoverflow.com/questions/24065460/attributeerror-nonetype-object-has-no-attribute-path-in-function-remove
from views.index import index as index_blueprint
app.register_blueprint(index_blueprint)

from views.photos import photos as photos_blueprint
app.register_blueprint(photos_blueprint)

# move show method to home.py
# @app.route('/')
# def show():
# 	return '<h1>Hello World</h1>'
