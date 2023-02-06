from flask import Blueprint
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

admin = Blueprint('admin', __name__, url_prefix='', template_folder='templates',
                  static_folder='static',
                  static_url_path='/admin/static')

maildaemon = Mail()

db = SQLAlchemy()
