from flask_login import UserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()

da = SQLAlchemy()


class User(da.Model, UserMixin):
    id = da.Column(da.Integer, primary_key=True)
    username = da.Column(da.String(20), unique=True, nullable=False)
    email = da.Column(da.String(120), unique=True, nullable=False)
    image_file = da.Column(da.String(20), nullable=False, default='default.jpg')
    password = da.Column(da.String(60), nullable=False)


