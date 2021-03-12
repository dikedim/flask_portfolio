"""Desktop dev pages."""
from flask import Blueprint, render_template
from flask import current_app as app
#from import flask_portfolio.api import fetch_jobs


desktop_bp = Blueprint(
    'desktop_bp', __name__,
    template_folder='templates'
)


@desktop_bp.route('/desktop', methods=['GET'])
def desk_port():
    return render_template("desktop_portfolio.html")


# @mobile_bp.route('/mobile/<int:mobile_id>/', methods=['GET'])
# def mobile_portf(mobile_id):
#    """Mobile development portfolio."""
#    jobs = fetch_jobs(app)[mobile_id]
#    return render_template("mobile_porfolio.html")
