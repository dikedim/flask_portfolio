from flask import render_template, request
from app.web import web_bp
from app.home.models import Jobs


#@web_bp.route('/web/<int:web_id>/', methods=['GET'])
#def web_portf(web_id):
#
#    jobs = fetch_jobs(app)[web_id]
#    return render_template("web_portfolio.html")


@web_bp.route('/portfolio/web', methods=['GET'])
def web():
    """Web development portfolio."""
    page = request.args.get('page', 1, type=int)
    #job = Jobs.query.order_by(Jobs.title.desc()).paginate(page=page, per_page=20, error_out=True)
    job = Jobs.query.filter_by(jobtype_id='4').paginate(page=page, per_page=10, error_out=True)
    return render_template("web_portfolio.html", jobs=job)

#
#@web_bp.route('/altindex')
#def altindex():
#    return render_template("index_bgcolor.html")
