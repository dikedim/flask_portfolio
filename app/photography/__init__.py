"""Photography pages."""
from flask import Blueprint, render_template
from flask import current_app as app
#from import flask_portfolio.api import fetch_jobs


photo_bp = Blueprint('photo_bp', __name__, template_folder='templates', static_url_path='app/static')


from . import routes
