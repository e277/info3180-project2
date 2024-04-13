# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, IntegerField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class PostForm(FlaskForm):
    caption = TextAreaField('Caption', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    user_id = IntegerField('UserID', validators=[InputRequired()])
    created_on = StringField('CreatedOn', validators=[InputRequired()])
    
class LikeForm(FlaskForm):
    post_id = IntegerField('PostID', validators=[InputRequired()])
    user_id = IntegerField('UserID', validators=[InputRequired()])
    
class FollowForm(FlaskForm):
    follower_id = IntegerField('FollowerID', validators=[InputRequired()])
    user_id = IntegerField('UserID', validators=[InputRequired()])
    
class UserForm:
    username = StringField('Username', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    profile_photo = FileField('ProfilePhoto', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    joined_on = StringField('JoinedOn', validators=[InputRequired()])

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