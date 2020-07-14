"""Photography pages."""
from flask import Blueprint, render_template
from flask import current_app as app
#from import flask_portfolio.api import fetch_jobs


photo_bp = Blueprint('photo_bp', __name__, template_folder='templates')


@photo_bp.route('/photography', methods=['GET'])
def photo_all():
    """Photography portfolio."""
    #jobs = fetch_jobs(app)[photo_id]
    return render_template("./photography_portfolio.html")


@photo_bp.route('/photography/<int:photo_id>/', methods=['GET'])
def photo_jobs(photo_id):
    """Photography portfolio."""
    #jobs = fetch_jobs(app)[photo_id]
    return render_template("photography_porfolio.html")
