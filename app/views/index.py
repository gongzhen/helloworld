from flask import Blueprint, render_template, abort, redirect, url_for, request
from jinja2 import TemplateNotFound
from . import index
import json, datetime
# move this line below to __init__.py
# index = Blueprint('index', __name__, template_folder='../template')

@index.route('/')
def index_show():
	return render_template('index.html')