from flask import Blueprint

index = Blueprint('index', __name__, template_folder='../templates')

photos = Blueprint('photos', __name__, template_folder='../templates')

# from . import index