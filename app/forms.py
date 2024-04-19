# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, IntegerField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class PostForm(FlaskForm):
    caption = TextAreaField('Caption', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    user_id = IntegerField('UserID', validators=[InputRequired()])
    
class LikeForm(FlaskForm):
    post_id = IntegerField('PostID', validators=[InputRequired()])
    user_id = IntegerField('UserID', validators=[InputRequired()])
    
class FollowForm(FlaskForm):
    follower_id = IntegerField('FollowerID', validators=[InputRequired()])
    user_id = IntegerField('UserID', validators=[InputRequired()])
    
class UserForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    profile_photo = FileField('ProfilePhoto', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
