from flask import render_template, request
from app.photography import photo_bp
from app.home.models import Jobs


@photo_bp.route('/portfolio/photography', methods=['GET'])
def photo():
    """Photography portfolio."""
#    #jobs = fetch_jobs(app)[photo_id]
    page = request.args.get('page', 1, type=int)
    job = Jobs.query.filter_by(jobtype_id='3').paginate(page=page, per_page=10, error_out=True)
    return render_template("photography_portfolio.html", jobs=job)


@photo_bp.route('/photography/<int:photo_id>/', methods=['GET'])
def photo_jobs(photo_id):
    """Photography portfolio."""
#    jobs = fetch_jobs(app)[photo_id]
    return render_template("photo_post.html")
