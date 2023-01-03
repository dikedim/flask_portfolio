from flask_wtf import FlaskForm
from wtforms import BooleanField, TextAreaField, SubmitField, StringField, SelectField, FileField
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


plan_types = ('0', 'Please select'), ('1', 'Basic'), ('2', 'Plus'), ('3', 'Pro'), ('4', 'Max')
additional_gigs = ('0', ''), ('1', 'Photo'), ('2', 'Complete Photography')


class OrderForm(FlaskForm):
    plan = SelectField(u"Plan", validators=[DataRequired("Please select a plan")], choices=plan_types, coerce=int)
    sub_plan = SelectField(u"Sub-Plan", choices=additional_gigs, coerce=int)
    name = StringField("Name", validators=[DataRequired("Please enter your name")])
    email = StringField("Email", validators=[DataRequired("Please enter your email address")])
    phone = StringField("Phone")
    description = TextAreaField("Message", validators=[DataRequired(" Can't send a blank message")])
    submit = SubmitField("Send Request")


class CommentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired("Please enter your name")])
    body = TextAreaField("Message", validators=[DataRequired(" Can't send a blank message")])
    submit = SubmitField("Add Comment")


class ClientsForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired("Please enter your name")])
    website = StringField("Name", validators=[DataRequired("Please enter your name")])
#    #logo = FileField("logo", default=)
    submit = SubmitField("Add Client")
