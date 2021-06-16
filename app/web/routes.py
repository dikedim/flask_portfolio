from flask import render_template
from app.web import web_bp


#@web_bp.route('/web/<int:web_id>/', methods=['GET'])
#def web_portf(web_id):
#    """Web development portfolio."""
#    jobs = fetch_jobs(app)[web_id]
#    return render_template("web_porfolio.html")


@web_bp.route('/web', methods=['GET'])
def web():
    return render_template("web_portfolio.html")


@web_bp.route('/altindex')
def altindex():
    return render_template("index_bgcolor.html")
