"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import render_template, request, jsonify, send_file
import os
from app.models import User, Like, Follow
from app.forms import PostForm, LikeForm, FollowForm, UserForm


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/users/{user_id}/posts', methods=['POST'])
# @auth.login_required
def add_posts(user_id):
    # Used for adding posts to the users feed
    post = PostForm()
    # get user id from authentification
    if request.method == 'POST' and post.validate_on_submit():
        caption = post.caption.data
        photo = post.photo.data
        user_id = post.user_id.data
        created_on = post.created_on.data
        return jsonify(message="Post added successfully", caption=caption, photo=photo, user_id=user_id, created_on=created_on)
    

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