from flask import Blueprint, render_template, abort, redirect, url_for, request
from jinja2 import TemplateNotFound
from . import index
import json, datetime
# move this line below to __init__.py
# index = Blueprint('index', __name__, template_folder='../template')

@index.route('/')
def show_index():
	return render_template('index.html')


@index.route('/about')
def about():
	return render_template('about.html')	

@index.route('/resume')
def resume():
	return render_template('resume.html')	

@index.route('/projects')
def projects():
	return render_template('projects.html')		

@index.route('/contacts')
def contacts():
	return render_template('contacts.html')			

