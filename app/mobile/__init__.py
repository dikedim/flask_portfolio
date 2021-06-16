"""Mobile dev pages."""
from flask import Blueprint
from flask import current_app as app
#from import flask_portfolio.api import fetch_jobs


mobile_bp = Blueprint(
    'mobile_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


from . import routes
