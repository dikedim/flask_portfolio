from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired("Please enter your name")])
    email = StringField("Email", validators=[DataRequired("Please enter your email address")])
    subject = StringField("Subject", validators=[DataRequired("Please enter a subject")])
    message = TextAreaField("Message", validators=[DataRequired(" Can't send a blank message")])
    submit = SubmitField("Send Message")


class Email:

    def email_confirm(self):
        body = "<html> <body> <p> {} </p> <br> <br>  <p> Lorem Ipsum is simply dummy text of the printing " \
               "and typesetting industry.</p> </body> </html>"
        return body

