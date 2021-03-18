from app.admin import admin
from flask import render_template
from flask_login import (current_user, login_required,login_user, logout_user, confirm_login)


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


@admin.route('/admin/mail', methods=['GET'])
def mail():
    return render_template("admin/mailbox.html")


@admin.route('/admin/compose', methods=['GET'])
def mail_compose():
    return render_template("admin/mailbox-compose.html")


@admin.route('/admin/inbox', methods=['GET'])
def inbox():
    return render_template("admin/mailbox-view.html")


@admin.route('/admin/lock', methods=['GET'])
def lock():
    return render_template("admin/lock.html")


@admin.route('/admin/register', methods=['GET'])
def password_recovery():
    return render_template("admin/register.html")
