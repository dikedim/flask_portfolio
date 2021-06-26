from app.admin import admin, maildaemon
from flask import (render_template, flash, redirect, url_for, request)
from flask_login import (current_user, login_required,login_user, logout_user, confirm_login)
from datetime import datetime
from .models import User, login_manager, da
from .forms import PostForm, EmailForm, LoginForm, JobForm
from app.home.models import Posts, Jobs
from flask_mail import Message, Mail


@admin.route('/admin', methods=['GET'])
def index():
    return render_template("admin/index.html")


@admin.route('/admin/login', methods=['GET'])
def login():
    return render_template("admin/login.html")


@admin.route('/admin/register', methods=['GET'])
def register():
    return render_template("admin/register.html")


@admin.route('/logout', methods=['GET'])
def logout():
    return render_template("admin/index.html")


@admin.route('/admin/inbox', methods=['GET'])
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


@admin.errorhandler(404)
def page_not_found(error):
    return render_template('admin/404.html'), 404


@admin.errorhandler(500)
def internal_error(error):
    return render_template('admin/500.html'), 500


@admin.route('/admin/files', methods=['GET'])
def file_manager():
    return render_template("admin/file-manager.html")


@admin.route('/admin/analytics', methods=['GET'])
def analytics():
    return render_template("admin/analytics.html")


@admin.route('/admin/blog', methods=['GET'])
def blogstats():
    return render_template("admin/blog.html")


@admin.route('/admin/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Posts(title=form.title.data, content=form.content.data, author='Admin')
        da.session.add(post)
        da.session.commit()
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
    if form.validate_on_submit():
        job = Jobs(title=form.title.data, content=form.content.data, link=form.link.data, photo=form.photo.data,
                   jobtype=form.category.data)
        da.session.add(job)
        da.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('admin.index'))
    return render_template('admin/jobs.html', form=form)
