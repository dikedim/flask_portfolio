from flask import Blueprint
from flask import current_app as app


 main_bp = Blueprint(
    'main_bp', __name__,
    template_foler='template',
    static_folder='static'
 )
