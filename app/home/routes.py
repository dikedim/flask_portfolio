import os, sqlalchemy, timeago
from app.home import home_bp, mailer
from flask import (Blueprint, render_template, request, redirect, url_for, flash, jsonify, send_from_directory,
                   send_file, current_app, render_template_string)
# from flask import current_app as app
from app.admin.routes import *
from app.admin import routes
from .forms import ContactForm, Email, OrderForm, CommentForm
from flask_mail import Message, Mail
import app as ap
from flask_wtf.csrf import CSRFError
from dotenv import load_dotenv
# import sqlalchemy as dba
from .models import Posts, Category, Jobs, JobType, Comments, db, Clients
from app.app import hcaptcha
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
MAP_BOX_KEY = os.environ.get('MAP_BOX_KEY')
JOB_IMAGES = os.environ.get('JOB_IMAGES')
CONTACT_MAIL = os.environ.get('CONTACT_MAIL')


@home_bp.route('/', methods=['GET', 'POST'])
def index():
#    load_clients()
    form = ContactForm()
    clients = Clients.query.all()
    # page = request.args.get('page', 1, type=int)
    # post = Posts.query.order_by(Posts.date_posted.desc()).paginate(page=page, per_page=5)
    #post = Posts.query.all()
    post = Posts.query.order_by(Posts.date_posted.desc()).limit(10)
    categories = Category.query.all()
    # jobber = Jobs.query.all()
    jobtype = JobType.query.all()
    #mapapi = MAP_BOX_KEY
    page = request.args.get('page', 1, type=int)
    job = Jobs.query.order_by(Jobs.title.desc()).paginate(page=page, per_page=12, error_out=True)

    if request.method == 'POST':
        if hcaptcha.verify():
            send_mail()
            message = 'Thanks, your message was sent successfully.'
            return render_template('index.html', success=True, posts=post, categories=categories, jobs=job,
                                   jobtypes=jobtype, message=message, mapapi=MAP_BOX_KEY, clients=clients)
        else:
            message = 'Please fill out the ReCaptcha!'
        return render_template('index.html', success=False, mapapi=MAP_BOX_KEY, form=form, posts=post, categories=categories,
                               jobs=job, jobtypes=jobtype, message=message, clients=clients)
    else:
        pass
#    MAP_BOX_KEY = os.environ.get('MAP_BOX_KEY')
        return render_template('index.html', mapapi=MAP_BOX_KEY, form=form, posts=post, categories=categories,
                               jobs=job, jobtypes=jobtype, clients=clients)


#def load_clients():
#        client = Clients.query.all()
#        return render_template_string('', client=client)


@home_bp.route('/blog', methods=['GET'])
def blog():
    # posts = Posts.query.all()
    page = request.args.get('page', 1, type=int)
    post = Posts.query.order_by(Posts.date_posted.desc()).paginate(page=page, per_page=5)
    category = Category.query.all()
    # posts = Posts.query.order_by(Posts.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("blog.html", posts=post, categories=category)


@home_bp.route('/blog/archive/<selected_date>', methods=['GET'])
def archive(selected_date):
    selected_date = Posts.date_posted.strftime(selected_date, "%b-%Y")
    page = request.args.get('page', 1, type=int)
    post = Posts.query.order_by(Posts.date_posted.desc()).paginate(page=page, per_page=5)
    category = Category.query.all()
    # posts = Posts.query.order_by(Posts.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("archive.html", posts=post, categories=category, selected_date=selected_date)


@home_bp.route('/blog/<string:slug>', methods=['GET', 'POST'])
def blog_post(slug):
    form = CommentForm()
## TODO Add nested comments
    post = Posts.query.filter_by(slug=slug).one()
    comments = Comments.query.all()
    if request.method == 'POST':
        if hcaptcha.verify():
            if form.validate():
                message = 'Thanks, your message was sent successfully.'
                comment = Comments(name=form.name.data, body=form.body.data)
                db.session.add(comment)
                db.session.commit()
                return render_template('blog-post.html', success=True, message=message, post=post, comments=comments)
            else:
                message = 'Please fill out the ReCaptcha!'
                flash('All fields are required.')
                return render_template('index.html', form=form, message=message, comments=comments)

    try:
        post = Posts.query.filter_by(slug=slug).one()
        return render_template("blog-post.html", title=post.title, post=post, slug=post.slug, comments=comments,
                               form=form)
    except sqlalchemy.orm.exc.NoResultFound:
        abort(404)


@home_bp.route('/jobs/', methods=['GET'])
def jobs():
    job = Jobs.query.all()
    jobtype = JobType.query.all()
    return render_template("jobs.html", job=job, jobtype=jobtype)


@home_bp.route('/mapbox', methods=['GET'])
def mapbox():
    return render_template("mapbox.html", mapapi=MAP_BOX_KEY)


@home_bp.errorhandler(404)
def page_not_found(e):
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
    page = request.args.get('page', 1, type=int)
    job = Jobs.query.order_by(Jobs.title.desc()).paginate(page=page, per_page=12, error_out=True)
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('index.html', form=form, mapapi=MAP_BOX_KEY)
        else:
            msg = Message(form.subject.data, sender=(form.name.data, form.email.data), recipients=[CONTACT_MAIL])
            msg.body = """
                  From: %s &lt;%s&gt;
                  %s
                  """ % (form.name.data, form.email.data, form.message.data)
            mailer.send(msg)
            # TODO #confirm_mail()
            return render_template('index.html', success=True, jobs=job, mapapi=MAP_BOX_KEY)

    elif request.method == 'GET':
        return render_template('index.html', form=form, mapapi=MAP_BOX_KEY)


@home_bp.route('/<filename>')
def job_photo(filename):
    #post = Posts()
    #filename = post.photo
    return send_from_directory(current_app.config['JOB_IMAGES'], filename) ##not in use
    #return send_file(JOB_IMAGES, attachment_filename=post.photo)


@home_bp.route('/portfolio', methods=['GET'])
def portfolio():
    jobtype = JobType.query.all()
    page = request.args.get('page', 1, type=int)
    job = Jobs.query.order_by(Jobs.title.desc()).paginate(page=page, per_page=12, error_out=True)
    return render_template('portfolio.html', jobs=job, jobtypes=jobtype)


@home_bp.route('/order', methods=['GET', 'POST'])
def order():
    form = OrderForm()
    return render_template('order.html', form=form)


@home_bp.route('/directions', methods=['GET'])
def directions():
    return render_template('directions.html', mapboxl=MAP_BOX_KEY)

