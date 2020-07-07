"""Mobile dev pages."""
from flask import Blueprint, render_template
from flask import current_app as app
#from import flask_portfolio.api import fetch_jobs


mobile_bp = Blueprint(
    'mobile_bp', __name__,
    template_folder='template',
    static_folder='static'
)


@mobile_bp.route('/mobile/<int:mobile_id>/', methods=['GET'])
def mobile_portf(mobile_id):
    """Mobile development portfolio."""
    jobs = fetch_jobs(app)[mobile_id]
    return render_template("mobile_porfolio.html")
