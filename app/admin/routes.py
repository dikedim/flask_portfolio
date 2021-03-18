from app.admin import admin
from flask import render_template
from flask_login import (current_user, login_required,login_user, logout_user, confirm_login)


@admin.route('/admin', methods=['GET'])
def index():
    return render_template("admin/index.html")


@admin.route('/login', methods=['GET'])
def index():
    return render_template("admin/login.html")


@admin.route('/register', methods=['GET'])
def index():
    return render_template("admin/register.html")


@admin.route('/logout', methods=['GET'])
def index():
    return render_template("admin/index.html")

