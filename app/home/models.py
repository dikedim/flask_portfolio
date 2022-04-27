# from sqlalchemy import Table, Column, Integer, String
# from sqlalchemy.orm import mapper
# from yourapplication.database import metadata, db_session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
# import sqlalchemy


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
    comments = db.relationship('Comments', backref='posts', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_blog(id):
        posts = Posts.query.filter_by(id=id).first()

        return posts

    def get_comments(self):
        return Comments.query.filter_by(post_id=Posts.id).order_by(Comments.posted_on)

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
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text)
    posted_on = db.Column(db.DateTime(), default=datetime.utcnow)
    post = db.relationship('Posts', secondary=post_comments, backref='posts', lazy=True)
    avatar = db.Column(db.String(255), nullable=False, default='/static/images/man1.jpg')
#    comments = db.relationship('Posts', secondary=post_comments, backref='comments', lazy=True)
    post_id = db.Column(db.Integer(), db.ForeignKey('posts.id'), nullable=False)

    @hybrid_property
    def post_comment_id(self):
        return self.posts.id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    def get_comment(id):
        comment = Comments.query.all(id=id)
        return comment

    def __repr__(self):
        return "<Comments:{}>".format(self.id, self.name)


class Clients(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=False, default='/static/images/clients/client_1.png')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    def __repr__(self):
        return "<Clients:{}>".format(self.id, self.name)
