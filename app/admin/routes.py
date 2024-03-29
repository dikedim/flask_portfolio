import flask

from app.admin import admin, maildaemon
import os
import imghdr
from dotenv import load_dotenv
from flask import (render_template, flash, redirect, url_for, request, abort, current_app)
from werkzeug.utils import secure_filename
from flask_login import (current_user, login_required, login_user, logout_user, confirm_login, UserMixin)
from datetime import datetime
from app.admin import db
from .models import User, login_manager, is_safe_url
from .forms import PostForm, EmailForm, LoginForm, JobForm, PublicationForm, ExperienceForm, CertificationForm, \
    DegreeForm
from app.home.models import Posts, Jobs
from flask_mail import Message, Mail


load_dotenv()
#JOB_IMAGES = os.environ.get('JOB_IMAGES')
IMAGE_EXTENSIONS = os.environ.get('IMAGE_EXTENSIONS')


@admin.route('/admin', methods=['GET'])
@login_required
def index():
    return render_template("admin/index.html")


@admin.route('/admin/login', methods=['GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user()
        flask.flash('Logged in successfully')
        next = flask.request.args.get('next')
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('admin.index'))
    return render_template("admin/login.html")


@admin.route('/admin/register', methods=['GET'])
def register():
    return render_template("admin/register.html")


@admin.route('/logout', methods=['GET'])
def logout():
    return render_template("admin/index.html")


@admin.route('/admin/inbox', methods=['GET'])
@login_required
def inbox():
    return render_template("admin/mailbox.html")


@admin.route('/admin/compose', methods=['GET', 'POST'])
def mail_compose():
    forma = EmailForm()
    if request.method == 'POST':
        compose_mail()
        return render_template('admin/mailbox-compose.html', success=True)
    else:
        pass
        #    MAP_BOX_KEY = os.environ.get('MAP_BOX_KEY')
        return render_template('admin/mailbox-compose.html', form=forma)


@admin.route('/admin/mail', methods=['GET'])
def mail():
    return render_template("admin/mailbox-view.html")


@admin.route('/admin/lock', methods=['GET'])
def lock():
    form = LoginForm()
    return render_template("admin/lock.html", now=datetime.utcnow(), form=form)


@admin.route('/admin/recovery', methods=['GET'])
def password_recovery():
    return render_template("admin/password-recovery.html")


@admin.route('/admin/pw_meter', methods=['GET'])
def pw_meter():
    return render_template("admin/password-meter.html")


@admin.errorhandler(404)
def page_not_found(e):
    return render_template('admin/404.html'), 404


@admin.errorhandler(500)
def internal_error(e):
    return render_template('admin/500.html'), 500


@admin.route('/admin/files', methods=['GET'])
def file_manager():
    return render_template("admin/file-manager.html")


@admin.route('/admin/analytics', methods=['GET'])
def analytics():
    return render_template("admin/analytics.html")


@admin.route('/admin/blog', methods=['GET'])
def blogstats():
    post_count = Posts.query.count()
    # counter for jinja  {{ post_query.count() }}
    return render_template("admin/blog.html")


@admin.route('/admin/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Posts(title=form.title.data, content=form.content.data, author='Admin', slug=form.slug.data,
                     subtitle=form.subtitle.data, category_id=form.category.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('admin.index'))
    return render_template('admin/blog_create.html', form=form)


@admin.route('/admin/pw', methods=['GET'])
def password_meter():
    return render_template("admin/password-meter.html")


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


def compose_mail():
    forma = EmailForm()
    # emailer = forma.email.data
    # name = request.args.get('name')
    if request.method == 'POST':
        if forma.validate() == False:
            flash('All fields are required.')
            return render_template('admin/mailbox-compose.html', form=forma)
        else:
            msg = Message(forma.subject.data, sender=('Shout from Dike', 'shout@dikedim.com'),
                          recipients=forma.rcpt_email.data)
            msg.body = """
                  From: %s &lt;%s&gt;
                  %s
                  """ % ('shout@dikedim.com', forma.rcpt_email.data, forma.message1.data)
            # msg.attach(forma.attachment.data.filename, )
            maildaemon.send(msg)
            # confirm_mail()
            return render_template('admin/mailbox-compose.html', success=True)

    elif request.method == 'GET':
        return render_template('admin/mailbox-compose.html', form=forma)


@admin.route('/admin/addjob', methods=['GET', 'POST'])
def addjob():
    form = JobForm()
    listStat = [('1', 'Mobile'), ('2', 'Video'), ('3', 'Photo'), ('4', 'Web'), ('5', 'Desktop')]
    # form.process()
    if form.validate_on_submit():
        m = form.photo.data
        files_ = secure_filename(m.filename)
        # upload_image()
        #file_extension = os.path.splitext(files_)[1]
        #if file_extension not in 'IMAGE_EXTENSIONS' or file_extension != validate_(m.stream):
        #    abort(400)

        file_path = os.path.join(current_app.config['JOB_IMAGES'], 'works', files_).replace("\\", "/")
        m.save(os.path.join(current_app.config['UPLOAD_FOLDER'], "works", files_))
        job = Jobs(title=form.title.data, content=form.content.data, link=form.link.data,
                   photo=file_path, jobtype_id=form.category.data)
        #form.process()
        db.session.add(job)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('admin.index'))
    return render_template('admin/jobs.html', form=form)


#def upload_image():
#    m = JobForm()
#    job_image = request.files['photo']
#    filename = secure_filename(job_image.filename)
#    if filename != '':
#        file_extension = os.path.splitext(filename)[1]
#        if file_extension not in 'IMAGE_EXTENSIONS' or file_extension != validate_(job_image.stream):
#            abort(400)
#        job_image.save(os.path.join('JOB_IMAGES', filename))
#        # filename = secure_filename(m.photo.data.filename)
#        # m.photo.data.save(JOB_IMAGES + filename)
#        print('file uploaded')
#    return redirect(url_for('addjob'))
#
#
def validate_(stream):
    header = stream.read(512)
    stream.seek(0)
    format_ = imghdr.what(None, header)
    if not format_:
        return None
    return '.' + (format_ if format_ != 'jpeg' else 'jpg')


@admin.route('/admin/portfolio', methods=['GET', 'POST'])
def portfolio():
    return render_template('admin/images-cropper.html')


@admin.route('/admin/portfolio/edit', methods=['GET', 'POST'])
def edit_portfolio():
    return render_template('admin/images-cropper.html')


@admin.route('/admin/portfolio/delete', methods=['GET', 'POST'])
def delete_portfolio():
    return render_template('admin/images-cropper.html')


@admin.route('/admin/products', methods=['GET', 'POST'])
def products():
    return render_template('admin/product-list.html')


@admin.route('/admin/product/edit', methods=['GET', 'POST'])
def product_edit():
    return render_template('admin/product-edit.html')


@admin.route('/admin/product/details', methods=['GET', 'POST'])
def product_page():
    return render_template('admin/product-detail.html')


@admin.route('/admin/cart', methods=['GET', 'POST'])
def cart():
    return render_template('admin/product-cart.html')


@admin.route('/admin/cart/payment', methods=['GET', 'POST'])
def payment():
    return render_template('admin/product-payment.html')


@admin.route('/admin/blog', methods=['GET', 'POST'])
def blog():
    return render_template('admin/blog.html')


@admin.route('/admin/blogpost', methods=['GET', 'POST'])
def blogpost():
    return render_template('admin/blog-details.html')


@admin.route('/admin/map', methods=['GET', 'POST'])
def mapbox():
    return render_template('admin/google-map.html')


@admin.route('/admin/cropper', methods=['GET', 'POST'])
def imagecropper():
    return render_template('admin/images-cropper.html')


@admin.route('/admin/chart', methods=['GET', 'POST'])
def chart():
    return render_template('admin/images-cropper.html')


@admin.route('/admin/upload', methods=['GET', 'POST'])
def upload():
    return render_template('admin/images-cropper.html')


@admin.route('/admin/add_publication', methods=['GET', 'POST'])
def add_pub():
    form = PublicationForm()
    return render_template('admin/add-publication.html', form=form)


@admin.route('/admin/publications', methods=['GET'])
def publications():
    return render_template('admin/publication.html')


@admin.route('/admin/add_experience', methods=['GET', 'POST'])
def add_exp():
    form = ExperienceForm()
    return render_template('admin/add-experience.html', form=form)


@admin.route('/admin/experience', methods=['GET'])
def experience():
    return render_template('admin/experience.html')


@admin.route('/admin/add_certification', methods=['GET', 'POST'])
def add_cert():
    form = CertificationForm()
    return render_template('admin/add-certification.html', form=form)


@admin.route('/admin/certification', methods=['GET'])
def certification():
    return render_template('admin/certification.html')


@admin.route('/admin/add_degree', methods=['GET', 'POST'])
def add_deg():
    form = DegreeForm()
    return render_template('Admin/add-degree.html', form=form)


@admin.route('/admin/degree', methods=['GET'])
def degree():
    return render_template('admin/degree.html')
