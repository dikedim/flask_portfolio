from flask import render_template
from app.video import video_bp
from app.home.models import Jobs


@video_bp.route('/portfolio/video', methods=['GET'])
def video():
    return render_template("video_portfolio.html")


# @mobile_bp.route('portfolio/video/<int:id>', methods=['GET'])
# def mobile_portf(id):
#    """Video development portfolio."""
#    jobs = fetch_jobs(app)[mobile_id]
#    return render_template("mobile_porfolio.html")
