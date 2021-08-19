from flask import render_template
from app.photography import photo_bp
from app.home.models import Jobs


@photo_bp.route('/portfolio/photography', methods=['GET'])
def photo():
    """Photography portfolio."""
#    #jobs = fetch_jobs(app)[photo_id]
    return render_template("photography_portfolio.html")


@photo_bp.route('/photography/<int:photo_id>/', methods=['GET'])
def photo_jobs(photo_id):
    """Photography portfolio."""
#    jobs = fetch_jobs(app)[photo_id]
    return render_template("photo_post.html")
