from flask import render_template, request
from app.desktop import desktop_bp
from app.home.models import Jobs


@desktop_bp.route('/desktop', methods=['GET'])
def desktop():
    page = request.args.get('page', 1, type=int)
    job = Jobs.query.filter_by(jobtype_id='5').paginate(page=page, per_page=10, error_out=True)
    return render_template("desktop_portfolio.html", jobs=job)


# @mobile_bp.route('/mobile/<int:mobile_id>/', methods=['GET'])
# def mobile_portf(mobile_id):
#    """Mobile development portfolio."""
#    jobs = fetch_jobs(app)[mobile_id]
#    return render_template("mobile_porfolio.html")
