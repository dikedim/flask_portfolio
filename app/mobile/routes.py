from app.mobile import mobile_bp
from flask import render_template


#@mobile_bp.route('/mobile/<int:mobile_id>/', methods=['GET'])
#def mobile_portf(mobile_id):
#    """Mobile development portfolio."""
#    jobs = fetch_jobs(app)[mobile_id]
#    return render_template("mobile_porfolio.html")


@mobile_bp.route('/mobile', methods=['GET'])
def mobile():
    return render_template("mobile_post.html")
