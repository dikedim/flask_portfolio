import os
from flask import (Blueprint, render_template, request, redirect, url_for, flash, jsonify)
from flask import current_app as app
from app.admin.routes import *
from app.admin import routes
from .forms import ContactForm
from flask_wtf.csrf import CSRFError
from dotenv import load_dotenv
#import sqlalchemy as dba
from flask_sqlalchemy import SQLAlchemy
load_dotenv()


MAP_BOX_KEY = os.getenv('MAP_BOX_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
#engine = da.create_engine('mysql+pymysql://root:ndzQWkym4#@localhost/db')

engine = os.getenv('DB_ENGINE')
db = SQLAlchemy()

#home_bp = Blueprint('home_bp', __name__, template_folder='templates')


#@home_bp.route('/', methods=['GET'])
#def index():
#    return render_template('index.html')


#@home_bp.route('/blog', methods=['GET'])
#def blog():
#    return render_template("blog.html")


#@home_bp.route('/blog_post', methods=['GET'])
#def blog_post():
#    return render_template("blog-post.html")


#@home_bp.errorhandler(404)
#def page_not_found(error):
#    return render_template('error_404.html'), 404


#@home_bp.errorhandler(500)
#def internal_server_error(e):
#    return render_template('error_500.html'), 500


#@home_bp.errorhandler(CSRFError)
#def handle_csrf_error(e):
#    return jsonify({"error": e.description}), 400


#@home_bp.route('/contact', methods=['GET', 'POST'])
#def contacts():
#    form = ContactForm()
#    if request.method == 'POST':
#        if form.validate() == False:
#            flash('All fields are required.')
#            return render_template('blog_create.html', form=form)
#        else:
#            return 'Form posted'

#    elif request.method == 'GET':
#        return render_template('blog_create.html', form=form)


#@home_bp.route('/create', methods=('GET', 'POST'))
#@login_required
#def create():
#    if request.method == 'POST':
#        title = request.form['title']
#        body = request.form['body']
#        error = None
#
#        if not title:
#            error = 'Title is required.'
#
#        if error is not None:
#            flash(error)
#        else:
#            db = get_db()
#            db.execute(
#                'INSERT INTO post (title, body, author_id)'
#                ' VALUES (?, ?, ?)',
#                    (title, body, g.user['id'])
#                )
#                db.commit()
#                return redirect(url_for('blog.index'))

#        return render_template('blog/create.html')


#@home_bp.route('/about', methods=['GET'])
#def about():
#    return render_template("index.html")
#    return redirect(url_for('home_bp.index') + '#about-card')
#    return redirect(url_for('home_bp.index') + '#aboutcard')


#@home_bp.route('/resume', methods=['GET'])
#def resume():
#    return render_template("index.html")
#    return redirect(url_for('home_bp.index') + '#resume-card')


#@home_bp.route('/contacts', methods=['GET', 'POST'])
#def contacts():
#    return render_template('index.html')
#def contact_us():
#    form = ContactForm()
#    if request.method == 'POST':
#        if form.validate() == False:
#           flash ('All fields are required.')
#           return render_template('index.html', form=form)
#        else:
#           return 'Form posted'
#
#    elif request.method == 'GET':
#        return render_template('index.html', form=form)
#    return redirect(url_for('home_bp.index'))
#    values = {"data": "works page <br><a href= #works-card>works page</a>"}
#    return render_template('index.html', **values)


#@home_bp.route('/portfolio')
#def works():
#    return render_template("index.html")
#    return redirect(url_for('home_bp.index') + '#works-card')
