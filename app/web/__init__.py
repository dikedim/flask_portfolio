"""Web dev pages."""
from flask import Blueprint, render_template

#from import flask_portfolio.api import fetch_jobs


web_bp = Blueprint(
    'web_bp', __name__,
    template_folder='templates'
)

from . import routes
