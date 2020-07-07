"""Web dev pages."""
from flask import Blueprint, render_template
from flask import current_app as app
#from import flask_portfolio.api import fetch_jobs


web_bp = Blueprint(
    'web_bp', __name__,
    template_folder='template',
    static_folder='static'
)


@mobile_bp.route('/web/<int:web_id>/', methods=['GET'])
def web_portf(web_id):
    """Web development portfolio."""
    jobs = fetch_jobs(app)[web_id]
    return render_template("web_porfolio.html")
