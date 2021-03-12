from flask import Flask, render_template, request
# from views import *
from .mobile import mobile_bp
from .photography import photo_bp
from .web import web_bp
from .home.main import home_bp
from .desktop import desktop_bp
from .video import video_bp


# app = Flask(__name__, static_url_path="")
app = Flask(__name__, template_folder="templates")
app.register_blueprint(mobile_bp)
app.register_blueprint(photo_bp)
app.register_blueprint(web_bp)
app.register_blueprint(home_bp)
app.register_blueprint(desktop_bp)
app.register_blueprint(video_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
