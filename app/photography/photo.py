"""Photography pages."""
from flask import Blueprint, render_template
from flask import current_app as app
#from import flask_portfolio.api import fetch_jobs


photo_bp = Blueprint(
    'photo_bp', __name__,
    template_folder='template',
    static_folder='static'
)


@mobile_bp.route('/photography/<int:photo_id>/', methods=['GET'])
def photo_portf(photo_id):
    """Photography portfolio."""
    jobs = fetch_jobs(app)[photo_id]
    return render_template("photography_porfolio.html")
