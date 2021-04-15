from flask import Blueprint
from flask_login import LoginManager


admin = Blueprint('admin', __name__, url_prefix='', template_folder='templates',
                  static_folder='static',
                  static_url_path='/admin/static')
