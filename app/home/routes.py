import os
from app.home import home_bp, mailer
from flask import (Blueprint, render_template, request, redirect, url_for, flash, jsonify, send_from_directory,
                   send_file, current_app)
from flask import current_app as app
from app.admin.routes import *
from app.admin import routes
from .forms import ContactForm, Email
from flask_mail import Message, Mail
import app as ap
from flask_wtf.csrf import CSRFError
from dotenv import load_dotenv
#import sqlalchemy as dba
from .models import Posts, Category, Jobs, JobType
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
MAP_BOX_KEY = os.environ.get('MAP_BOX_KEY')
JOB_IMAGES = os.environ.get('JOB_IMAGES')


@home_bp.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    # page = request.args.get('page', 1, type=int)
    # post = Posts.query.order_by(Posts.date_posted.desc()).paginate(page=page, per_page=5)
    post = Posts.query.all()
    categories = Category.query.all()
    job = Jobs.query.all()
    jobtype = JobType.query.all()
    if request.method == 'POST':
        send_mail()
        return render_template('index.html', success=True, posts=post, categories=categories, jobs=job, jobtypes=jobtype)
    else:
        pass
#    MAP_BOX_KEY = os.environ.get('MAP_BOX_KEY')
        return render_template('index.html', mapapi=MAP_BOX_KEY, form=form, posts=post, categories=categories,
                               jobs=job, jobtypes=jobtype)


@home_bp.route('/blog', methods=['GET'])
def blog():
    # posts = Posts.query.all()
    page = request.args.get('page', 1, type=int)
    post = Posts.query.order_by(Posts.date_posted.desc()).paginate(page=page, per_page=5)
    categories = Category.query.all()
    # posts = Posts.query.order_by(Posts.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("blog.html", posts=post, categories=categories)


@home_bp.route('/blog_post/<int:post_id>', methods=['GET'])
def blog_post(post_id):
    # posts = Posts.query.get_or_404(posts_id)
    post = Posts.query.filter_by(id=post_id).one()
    return render_template("blog-post.html", title=post.title, posts=post)


@home_bp.route('/jobs/', methods=['GET'])
def jobs():
    job = Jobs.query.all()
    jobtype = JobType.query.all()
    return render_template("jobs.html", job=job, jobtype=jobtype)


@home_bp.route('/mapbox', methods=['GET'])
def mapbox():
    return render_template("mapbox.html")


@home_bp.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html'), 404


@home_bp.errorhandler(500)
def internal_server_error(e):
    return render_template('error_500.html'), 500


@home_bp.errorhandler(CSRFError)
def handle_csrf_error(e):
    return jsonify({"error": e.description}), 400


def confirm_mail():
    forms = ContactForm()
    msg = Message("Re: Confirmation of email receipt from https://dikedim.com",
                  sender=('Dike Dim', "shout@dikedim.com"),
                  recipients=[forms.email.data])
    msg.html = render_template('email_confirmation.html')

    mailer.send(msg)


# @home_bp.route('/', methods=['GET', 'POST'])
def send_mail():
    form = ContactForm()
    emailer = form.email.data
    name = request.args.get('name')
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('index.html', form=form, MAP_BOX_KEY=MAP_BOX_KEY)
        else:
            msg = Message(form.subject.data, sender=(form.name.data, form.email.data), recipients=['shout@dikedim.com'])
            msg.body = """
                  From: %s &lt;%s&gt;
                  %s
                  """ % (form.name.data, form.email.data, form.message.data)
            mailer.send(msg)
            # TODO #confirm_mail()
            return render_template('index.html', success=True)

    elif request.method == 'GET':
        return render_template('index.html', form=form, MAP_BOX_KEY=MAP_BOX_KEY)


@home_bp.route('/<filename>')
def job_photo(filename):
    #post = Posts()
    #filename = post.photo
    return send_from_directory(current_app.config['JOB_IMAGES'], filename)
    #return send_file(JOB_IMAGES, attachment_filename=post.photo)
