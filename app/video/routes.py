from flask import render_template
from app.video import video_bp


@video_bp.route('/video', methods=['GET'])
def video():
    return render_template("video_portfolio.html")


# @mobile_bp.route('/mobile/<int:mobile_id>/', methods=['GET'])
# def mobile_portf(mobile_id):
#    """Mobile development portfolio."""
#    jobs = fetch_jobs(app)[mobile_id]
#    return render_template("mobile_porfolio.html")
