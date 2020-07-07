from run import app
from flask import render_template, url_for, redirect, request


@app.route('/error_404')
def error_404():
    return render_template("error_404.html")


@app.route('/post')
def blog_post():
    return render_template("blog-post.html")


@app.route('/blog')
def blog():
    return render_template("blog.html")


@app.route('/')
def index():
    return render_template("index-bgcolor.html")
