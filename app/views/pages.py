from flask import Blueprint, render_template, abort, redirect, url_for, request
from jinja2 import TemplateNotFound
import json, datetime
from . import pages

@pages.route('/<path:path>')
def show_page(path):
	try:
		if not page:
			abort(404)
	return render_template('page.html')

