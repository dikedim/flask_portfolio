from app.mobile import mobile_bp
from flask import render_template, request
from app.home.models import Jobs


#@mobile_bp.route('/mobile/<int:mobile_id>/', methods=['GET'])
#def mobile_portf(mobile_id):
#    """Mobile development portfolio."""
#    jobs = fetch_jobs(app)[mobile_id]
#    return render_template("mobile_porfolio.html")


@mobile_bp.route('/portfolio/mobile', methods=['GET'])
def mobile():
    #job = Jobs.query.filter_by(id=jobtype_id).one()
    page = request.args.get('page', 1, type=int)
    # job = Jobs.query.order_by(Jobs.title.desc()).paginate(page=page, per_page=20, error_out=True)
    job = Jobs.query.filter_by(jobtype_id='1').paginate(page=page, per_page=10, error_out=True)
    return render_template("mobile_portfolio.html", jobs=job)
