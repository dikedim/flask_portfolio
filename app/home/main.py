from flask import Blueprint, render_template, request, redirect, url_for
from flask import current_app as app

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


@home_bp.route('/about', methods=['GET'])
def about_card():
    return redirect(url_for('home_bp.index') + '#about-card')


@home_bp.route('/resume', methods=['GET'])
def resume_card():
    return redirect(url_for('home_bp.index') + '#resume-card')
