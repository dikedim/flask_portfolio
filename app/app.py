from flask import Flask
# from views import *
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
from .home.models import db
from .admin.models import da
from .admin.models import login_manager


# app = Flask(__name__, static_url_path="")
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
    mailer.init_app(app)
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    register_admin(app)
    register_blog(app)
    register_blueprints(app)

    return app


# if __name__ == '__main__':
#    app.run(host="0.0.0.0")
#    app.config.from_object('settings.DevelopmentConfig')
