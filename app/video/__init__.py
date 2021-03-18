"""Video dev pages."""
from flask import Blueprint, render_template
from flask import current_app as app
#from import flask_portfolio.api import fetch_jobs


video_bp = Blueprint(
    'video_bp', __name__,
    template_folder='templates'
)


@video_bp.route('/video', methods=['GET'])
def vid_port():
    return render_template("video_portfolio.html")


# @mobile_bp.route('/mobile/<int:mobile_id>/', methods=['GET'])
# def mobile_portf(mobile_id):
#    """Mobile development portfolio."""
#    jobs = fetch_jobs(app)[mobile_id]
#    return render_template("mobile_porfolio.html")
