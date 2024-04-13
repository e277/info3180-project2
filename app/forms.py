from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(max=80)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=128)])
    firstname = StringField('First Name', validators=[InputRequired(), Length(max=80)])
    lastname = StringField('Last Name', validators=[InputRequired(), Length(max=80)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=80)])
    location = StringField('Location', validators=[Length(max=80)])
    biography = StringField('Biography', validators=[Length(max=1000)])
    profile_photo = FileField('File', 
                    validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])