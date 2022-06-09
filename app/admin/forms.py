from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms.validators import InputRequired, Email, DataRequired, EqualTo
from wtforms import PasswordField, StringField, SubmitField, TextAreaField, FileField, SelectField, DateField


class LoginForm(FlaskForm):
    username = StringField('Username', id='username_login', validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login', validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('Username', id='username_create', validators=[DataRequired()])
    email = StringField('Email', id='email_create', validators=[DataRequired(), Email()])
    password = PasswordField('Password', id='pwd_create', validators=[DataRequired()])


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')


class RequestReset(FlaskForm):
    username = StringField('Username', id='username_create', validators=[DataRequired()])
    email = StringField('Email', id='email_create', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


post_categories = ('0', ''), ('1', 'Travel'), ('2', 'Photography'), ('3', 'Coding'), ('4', 'Writing')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])
    subtitle = StringField('subtitle')
    category = SelectField(u'Category', validators=[DataRequired()], choices=post_categories, coerce=int)
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


#    def validate_email(self, email):
#        user = User.query.filter_by(email=email.data).first()
#        if user is None:
#            raise ValidationError('There is no account with that email. You must register first.')

class EmailForm(FlaskForm):
    sndr_email = StringField("Sender Email", description="Please enter your email address", default="shot@dikedim.com")
    rcpt_email = StringField("Recipient Email", validators=[DataRequired("Please enter recipient email address")])
    cc = StringField("cc", description="copy address")
    bcc = StringField("bcc", description="blind copy addresses")
    dummy = StringField("dummy")
    attachment = FileField("attachments")
    subject = StringField("Subject", validators=[DataRequired("Please enter a subject")])
    message1 = TextAreaField("Message")
    submit = SubmitField("Send Message")


class JobForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    link = StringField('Link')
    # category = StringField('Category', validators=[DataRequired()])
    category = SelectField(u'Category',
                           choices=[('0', ''), ('1', 'Mobile'), ('2', 'Video'), ('3', 'Photo'), ('4', 'Web'),
                                    ('5', 'Desktop')])
    content = TextAreaField('Content')
    photo = FileField("Attachments", validators=[FileRequired(),
                                                 FileAllowed(['jpg', 'jpeg', 'gif' 'png', 'tiff', 'bmp'],
                                                             'Images only!')])

    submit = SubmitField('Post')


class BlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    link = StringField('Link')
    slug = StringField('Slug')
    # category = StringField('Category', validators=[DataRequired()])
    category = SelectField(u'Category', choices=[('0', ''), ('1', 'Travel'), ('2', 'Video'), ('3', 'Photo')])
    content = TextAreaField('Content')
    photo = FileField("Attachments", validators=[FileRequired(),
                                                 FileAllowed(['jpg', 'jpeg', 'gif' 'png', 'tiff', 'bmp'],
                                                             'Images only!')])

    submit = SubmitField('Post')


class PublicationForm(FlaskForm):
    authors = StringField('Authors: ', validators=[DataRequired()])
    link = StringField('Link: ')
    title = StringField('Title: ')
    page = StringField('Page: ')
    language = SelectField(u'Language: ', choices=[('0', ''), ('1', 'English'), ('2', 'Russian'), ('3', 'Other')])
    journal = StringField('Journal: ')
    submit = SubmitField('Add Publication')


class CertificationForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    date = DateField('Date:', format='%d-%m-%Y')
    mode = SelectField(u'Mode: ', choices=[('0', ''), ('1', 'In-Person'), ('2', 'Online'), ('3', 'Hybrid')])
    title = StringField('Title: ')
    organization = StringField('Issuing Organization: ')
    location = StringField('Location: ')
    certificate = FileField('Certificate: ', validators=[FileRequired()])
    submit = SubmitField('Add certification')


class ExperienceForm(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    date_from = DateField('Date From', format='%m-%Y')
    date_to = DateField('Date To', format='%m-%Y')
    company = StringField('Company: ', validators=[DataRequired()])
    sub = StringField('Subheading')
    submit = SubmitField('Add Experience')


class DegreeForm(FlaskForm):
    school = StringField('School: ')
    date_from = DateField('Date From', format='%m-%Y', validators=[DataRequired()])
    date_to = DateField('Date To', format='%m-%Y')
    major = StringField('Major: ')
    city = StringField('City: ')
    faculty = StringField('Faculty: ')
    degree = FileField(' Attach Certifcate: ')
    submit = SubmitField('Add Degree')
