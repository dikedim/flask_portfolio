from flask import render_template
from app.desktop import desktop_bp


@desktop_bp.route('/desktop', methods=['GET'])
def desktop():
    return render_template("desktop_portfolio.html")


# @mobile_bp.route('/mobile/<int:mobile_id>/', methods=['GET'])
# def mobile_portf(mobile_id):
#    """Mobile development portfolio."""
#    jobs = fetch_jobs(app)[mobile_id]
#    return render_template("mobile_porfolio.html")
