from flask import Blueprint, render_template, request, redirect, url_for
from flask import current_app as app
from app.admin.routes import *
from app.admin import routes

home_bp = Blueprint('home_bp', __name__, template_folder='templates')


@home_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@home_bp.route('/blog', methods=['GET'])
def blog():
    return render_template("blog.html")


@home_bp.route('/blog_post', methods=['GET'])
def blog_post():
    return render_template("blog-post.html")


@home_bp.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html'), 404


@home_bp.route('/about', methods=['GET'])
def about():
    return render_template("index.html")
#    return redirect(url_for('home_bp.index') + '#about-card')
#    return redirect(url_for('home_bp.index') + '#aboutcard')


@home_bp.route('/resume', methods=['GET'])
def resume():
    return render_template("index.html")
#    return redirect(url_for('home_bp.index') + '#resume-card')


@home_bp.route('/contacts')
def contacts():
    return render_template('index.html')
#    return redirect(url_for('home_bp.index'))
#    values = {"data": "works page <br><a href= #works-card>works page</a>"}
#    return render_template('index.html', **values)


@home_bp.route('/portfolio')
def works():
    return render_template("index.html")
#    return redirect(url_for('home_bp.index') + '#works-card')
