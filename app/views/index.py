from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
import json, datetime

home = Blueprint('home', __name__, template_folder='../template')

@home.route('/')
def index():
    user = {'nickname':'Gong Zhen'}
    posts = [
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    print posts
    return render_template('index.html',
        title = 'Home',
        user = user,
        posts = posts)