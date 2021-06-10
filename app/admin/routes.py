from app.admin import admin
from flask import render_template
from flask_login import (current_user, login_required,login_user, logout_user, confirm_login)
from datetime import datetime
from .models import User, login_manager
from .forms import PostForm


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


@admin.route('/admin/compose', methods=['GET'])
def mail_compose():
    return render_template("admin/mailbox-compose.html")


@admin.route('/admin/mail', methods=['GET'])
def mail():
    return render_template("admin/mailbox-view.html")


@admin.route('/admin/lock', methods=['GET'])
def lock():
    return render_template("admin/lock.html", now=datetime.utcnow())


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


@admin.route('/admin/create_post', methods=['GET'])
def create_post():
    post = PostForm()
    return render_template("admin/blog_create.html", post=post)


@admin.route('/admin/pw', methods=['GET'])
def password_meter():
    return render_template("admin/password-meter.html")


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

