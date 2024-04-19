"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, jsonify, send_file, url_for
import os
from app.models import User, Like, Follow, Post
from app.forms import PostForm, LikeForm, FollowForm, UserForm
from datetime import datetime
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


@app.route('/api/v1/register', methods=['POST'])
def register():
    form = UserForm()  
    if form.validate_on_submit():  
        username = form.username.data
        password = form.password.data
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        location = form.location.data
        biography = form.biography.data
        # profile_photo = form.profile_photo.data
        profile_photo = form.profile_photo.data
        
        filename = secure_filename(profile_photo.filename)
        # profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        new_user = User(
            username = username,
            password = password,
            firstname = firstname,
            lastname = lastname,
            email = email,
            location = location,
            biography = biography,
            profile_photo = filename
        )
        
        db.session.add(new_user)
        db.session.commit() 
        
        return jsonify({"message": "User registered successfully"}), 200
    else:
        errors = form.errors 
        return jsonify({"errors": errors}), 400


@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is not None and check_password_hash(user.password, password):
            login_user(user)
            return jsonify({"message": "User logged in successfully"}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 400
    return jsonify({"errors": form.errors}), 400

@app.route("/api/v1/auth/logout", methods=['POST'])
@login_required
def logout():
    try: 
        logout_user()
        return jsonify({"message": "User logged out successfully"}), 200
    except Exception as e:
        return jsonify({"errors": str(e)}), 400

    
# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(User).filter_by(id=id)).scalar()
    return db.session.execute(db.select(User).filter_by(id=id)).scalar()


@app.route('/api/v1/users/<int:user_id>/posts', methods=['POST'])
# @auth.login_required
def add_posts(user_id):
    # Used for adding posts to the users feed
    post_form = PostForm()
    # get user id from authentication
    if post_form.validate_on_submit():
        caption = post_form.caption.data
        photo = post_form.photo.data
        user_id = post_form.user_id.data
        
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        post = Post(caption=caption, photo=filename, user_id=user_id) 
        db.session.add(post)
        db.session.commit()
        
        post_data = {
            "caption": post.caption,
            "user_id": post.user_id
        }
        
        return jsonify(message="Post added successfully", post=post_data), 201
    else:
        return jsonify(errors=form_errors(post_form)), 400

@app.route('/api/v1/users/{user_id}/posts', methods=['GET'])
# @auth.login_required
def get_posts(user_id):
    # Returns a user's posts
    pass

@app.route('/api/users/{user_id}/follow', methods=['POST'])
# @auth.login_required
def follow_user(user_id):
    # Create a Follow relationship between the current user and the target user.
    pass

@app.route('/api/v1/posts', methods=['GET'])
# @auth.login_required
def get_all_posts():
    # Return all posts for all users
    pass
    
app.route('/api/v1/posts/{post_id}/like', methods=['POST'])
# @auth.login_required
def like_post(post_id):
    # Set a like on the current Post by the logged in User
    pass


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404