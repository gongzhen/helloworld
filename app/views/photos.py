from flask import Blueprint, render_template, abort, redirect, url_for, request
from jinja2 import TemplateNotFound
from . import photos
import json, datetime

@photos.route('/banner')
def show_banner():
	return render_template('photos-banner.html')
