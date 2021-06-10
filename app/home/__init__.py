from flask import Blueprint
from flask_mail import Mail

home_bp = Blueprint('home_bp', __name__, template_folder='templates',
                    static_folder='static',
                    static_url_path='/home/static')
mailer = Mail()
