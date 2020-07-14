from flask import Flask, render_template, request
#from views import *
from .mobile.mobile import mobile_bp
from .photography.photo import photo_bp
from .web.web import web_bp
from .home.main import home_bp


#app = Flask(__name__, static_url_path="")
app = Flask(__name__)
app.register_blueprint(mobile_bp)
app.register_blueprint(photo_bp)
app.register_blueprint(web_bp)
app.register_blueprint(home_bp)


if __name__ == '__main__':
    app.run(debug=True)
