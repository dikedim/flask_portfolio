from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
# from yourapplication.database import metadata, db_session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlalchemy


db = SQLAlchemy()

post_tags = db.Table('posts_tags', db.Column('posts_id', db.Integer, db.ForeignKey('posts.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')))

job_types = db.Table('job_types', db.Column('jobs_id', db.Integer, db.ForeignKey('jobs.id')),
                     db.Column('jobtypes_id', db.Integer, db.ForeignKey('jobtypes.id')))

post_comments = db.Table('posts_comments', db.Column('comments_id', db.Integer, db.ForeignKey('comments.id')),
                         db.Column('posts_id', db.Integer, db.ForeignKey('posts.id')))


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    subtitle = db.Column(db.String(255))
    content = db.Column(db.Text)
    author = db.Column(db.String(255))
    photo = db.Column(db.String(255), nullable=False, default='/static/images/blog/blog1.jpg')
    date_posted = db.Column(db.DateTime(), default=datetime.utcnow)
    slug = db.Column(db.String(255))
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer(), db.ForeignKey('categories.id'))
    comments = db.relationship('Comments', backref='title', lazy='dynamic')

#    def get_comments(self):
#        return Comments.query.filter_by(post_id=posts.id).order_by(Comments.posted_on.desc())

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.title[:10])


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    posts = db.relationship('Posts', secondary=post_tags, backref='tags', lazy=True)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    posts = db.relationship('Posts', backref='categories', cascade='all,delete-orphan')

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)


class Jobs(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    link = db.Column(db.String(255))
    photo = db.Column(db.String(255), nullable=False, default='/static/images/works/work1.jpg')
    _jobtypes = db.relationship('JobType', secondary='job_types', backref=db.backref('jobs', lazy='dynamic'))
    jobtype_id = db.Column(db.Integer(), db.ForeignKey('jobtypes.id'))

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.title[:10])


class JobType(db.Model):
    __tablename__ = 'jobtypes'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
#    #jobs = db.relationship('Jobs', backref='jobtypes', cascade='all,delete-orphan')

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text)
    posted_on = db.Column(db.DateTime(), default=datetime.utcnow)
    avatar = db.Column(db.String(255), nullable=False, default='/static/images/man1.jpg')
#    comments = db.relationship('Posts', secondary=post_comments, backref='comments', lazy=True)
    post_id = db.Column(db.Integer(), db.ForeignKey('posts.id'))

    def __repr__(self):
        return "<Comments:{}>".format(self.id, self.name)

