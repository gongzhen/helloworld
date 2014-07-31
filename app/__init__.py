from flask import Flask, request, render_template

app = Flask(__name__)

# http://stackoverflow.com/questions/24065460/attributeerror-nonetype-object-has-no-attribute-path-in-function-remove
from views.index import home
app.register_blueprint(home)

# move show method to home.py
# @app.route('/')
# def show():
# 	return '<h1>Hello World</h1>'
