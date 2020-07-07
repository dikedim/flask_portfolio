from flask import Flask, render_template, request
from views import *
from mobile_porfolio.mobile import mobile_bp
from photography.photo import photo_bp
from web_portfolio.web import web_bp


app = Flask(__name__)
app.register_blueprint(mobile_bp)
app.register_blueprint(photo_bp)
app.register_blueprint(web_bp)


if __name__ == '__main__':
    app.run()
