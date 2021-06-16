from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
# from yourapplication.database import metadata, db_session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlalchemy


db = SQLAlchemy()

post_tags = db.Table('posts_tags', db.Column('posts_id', db.Integer, db.ForeignKey('posts.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')))


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    subtitle = db.Column(db.String(255))
    content = db.Column(db.Text)
    author = db.Column(db.String(255))
    photo = db.Column(db.String(20), nullable=False, default='default.jpg')
    date_posted = db.Column(db.DateTime)
    slug = db.Column(db.String(255))
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer(), db.ForeignKey('categories.id'))

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.title[:10])


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    # slug = db.Column(db.String(255), nullable=False)
    # created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    posts = db.relationship('Posts', secondary=post_tags, backref='tags', lazy=True)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    posts = db.relationship('Posts', backref='categories', cascade='all,delete-orphan')
    # posts_id = db.Column(db.Integer(), db.ForeignKey('posts.id'))

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)
