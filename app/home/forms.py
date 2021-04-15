from flask import Flask
from flask_mail import Mail, Message
from ..app import app
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired

mail = Mail(app)

app.config['MAIL_SERVER']='mail.dikedim.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'shout@dikedim.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.config['SECRET_KEY'] = 'cghiedincicniernveomvtemfkvmto'
# mail = Mail(app)


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")


