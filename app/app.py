from flask import Flask, current_app
# from views import *
import os
from . import hcaptcha
from .mobile import mobile_bp
from .photography import photo_bp
from .web import web_bp
from .desktop import desktop_bp
from .video import video_bp
from .home.routes import home_bp
from .admin import admin
from .home import mailer
# from .home.main import *
# from .home.forms import *
from flask_wtf.csrf import CSRFProtect
from .home.models import db, Category, JobType
from .admin.models import da
from .admin.models import login_manager
from dotenv import load_dotenv
from sqlalchemy import event
from app.home.routes import page_not_found, internal_server_error
#from flask_hcaptcha import hCaptcha
from sqlalchemy.event import listen


#hcaptcha = hCaptcha(app)


# app = Flask(__name__, static_url_path="")
# dotenv_path = os.path.join('BASE_DIR', 'app/')
# @event.listens_for(Category.__table__, 'after_create')
def post_category_values(*args, **kwargs):
    db.session.add(Category(name='Travel'))
    db.session.add(Category(name='Photography'))
    db.session.add(Category(name='Coding'))
    db.session.add(Category(name='Writing'))
    db.session.commit()


event.listen(Category.__table__, 'after_create', post_category_values)


def job_category_values(*args, **kwargs):
    db.session.add(JobType(name='Mobile'))
    db.session.add(JobType(name='Video'))
    db.session.add(JobType(name='Photography'))
    db.session.add(JobType(name='Web'))
    db.session.add(JobType(name='Desktop'))
    # db.session.add(JobType(name='Design'))
    db.session.commit()


event.listen(JobType.__table__, 'after_create', job_category_values)

app_folder = os.path.expanduser('/app')
load_dotenv(os.path.join(app_folder, '.env'))
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')


def register_admin(app):
    da.init_app(app)
    login_manager.init_app(app)


def register_blog(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def register_blueprints(app):
    app.register_blueprint(mobile_bp)
    app.register_blueprint(photo_bp)
    app.register_blueprint(web_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(desktop_bp)
    app.register_blueprint(video_bp)
    app.register_blueprint(admin)


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object('config.DevelopmentConfig')
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    mailer.init_app(app)
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    register_admin(app)
    register_blog(app)
    register_blueprints(app)
    hcaptcha.init_app(app)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
    # insert_initial_values()
    load_dotenv()

    return app


# if __name__ == '__main__':
#    app.run(host="0.0.0.0")
#    app.config.from_object('settings.DevelopmentConfig')
