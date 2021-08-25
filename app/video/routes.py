from flask import render_template, request
from app.video import video_bp
from app.home.models import Jobs


@video_bp.route('/portfolio/video', methods=['GET'])
def video():
    page = request.args.get('page', 1, type=int)
    job = Jobs.query.filter_by(jobtype_id='2').paginate(page=page, per_page=10, error_out=True)
    return render_template("video_portfolio.html", jobs=job)


# @mobile_bp.route('portfolio/video/<int:id>', methods=['GET'])
# def mobile_portf(id):
#    """Video development portfolio."""
#    jobs = fetch_jobs(app)[mobile_id]
#    return render_template("mobile_porfolio.html")
