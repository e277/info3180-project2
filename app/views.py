"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, jsonify, send_file, url_for, g, send_from_directory
import os
from app.models import User, Like, Follow, Post
from app.forms import PostForm, LikeForm, FollowForm, UserForm, LoginForm
from datetime import datetime
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf

import jwt
from functools import wraps
import datetime

app.config['WTF_CSRF_ENABLED'] = False #Comment out

###
# Routing for your application.
###
def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.headers.get('Authorization', None) # or request.cookies.get('token', None)

    if not auth:
      return jsonify({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'}), 401

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}), 401
    elif len(parts) == 1:
      return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
    elif len(parts) > 2:
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}), 401

    token = parts[1]
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])

    except jwt.ExpiredSignatureError:
        return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
    except jwt.DecodeError:
        return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

    g.current_user = user = payload
    return f(*args, **kwargs)

  return decorated

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()}), 200

@app.route('/api/v1/generate-token', methods=['GET'])
def generate_token():
    payload = {
        'sub': current_user.id,  # subject
        'name': current_user.username,  # username
        'iat': datetime.datetime.now(datetime.timezone.utc),  # issued at time
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)  # expiration time
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return {'jwt_token': token, 'user_id': current_user.id}

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
        profile_photo = form.profile_photo.data
        
        filename = secure_filename(profile_photo.filename)
        profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        user = User.query.filter_by(username=username).first()
        if user is None:
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
            return jsonify(errors="Username already exists"), 400
    else:
        return jsonify(errors=form_errors(form)), 400

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

        if user is not None and check_password_hash(user.password, password):
            login_user(user)
            token_info = generate_token()
            return jsonify({
                "message": "User logged in successfully",
                "jwt_token": token_info['jwt_token'],
                "user_id": token_info['user_id']
            }), 200
        else:
            return jsonify({"errors": "Invalid username or password"}), 400
    else:
        return jsonify({"errors": form_errors(form)}), 400

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

@app.route('/api/v1/users/<int:user_id>/posts', methods=['POST'])
@requires_auth
def add_posts(user_id):
    # Used for adding posts to the users feed
    form = PostForm()
    # get user id from authentication
    if form.validate_on_submit():
        # get the csrf_token from the authorization header
        
        caption = form.caption.data
        photo = form.photo.data
        user_id = form.user_id.data
        
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
        return jsonify(errors=form_errors(form)), 400

@app.route('/api/v1/users/<int:user_id>/posts', methods=['GET'])
@requires_auth
def get_posts(user_id):
    # Returns a user's posts
    user_posts = Post.query.filter_by(user_id=user_id).all()
    posts = []
    photos = get_uploaded_photos()
    
    if user_posts is not None and len(user_posts) > 0:
        for post in user_posts:
            if post.photo in photos:
                post.photo = url_for('uploaded_photo', photo=post.photo)
            
            posts_count = Post.query.filter_by(user_id=user_id).count()
            
            posts.append({
                "id": post.id,
                "user_id": post.user_id,
                "photo": post.photo,
                "caption": post.caption,
                "created_on": post.created_on,
                "total_posts": posts_count
            })
        return jsonify(posts=posts), 200
    else:
        return jsonify(message="No posts found for user"), 200

@app.route('/api/users/<int:user_id>/follow', methods=['POST'])
@requires_auth
def follow_user(user_id):
    current_user_id = g.current_user['sub']
    if current_user_id == user_id:
        return jsonify({'error': 'You cannot follow yourself'}), 400

    target_user = User.query.get(user_id)
    if not target_user:
        return jsonify({'error': 'User not found'}), 404

    existing_follow = Follow.query.filter_by(follower_id=current_user_id, user_id=user_id).first()
    if existing_follow:
        return jsonify({'error': 'You are already following this user', 'following': True}), 200

    new_follow = Follow(follower_id=current_user_id, user_id=user_id)
    db.session.add(new_follow)
    db.session.commit()

    # Assuming a followers relationship defined through Follow model or similar approach
    follower_count = Follow.query.filter_by(user_id=user_id).count()

    return jsonify({
        'message': 'You are now following {}'.format(target_user.username),
        'following': True,
        'follower_count': follower_count  # Update follower count dynamically
    }), 201

@app.route('/api/v1/posts', methods=['GET'])
# @requires_auth TODO: uncomment
def get_all_posts():
    # Return all posts for all users
    posts = Post.query.all()
    all_posts = []
    photos = get_uploaded_photos()
    
    if posts is not None and len(posts) > 0:
        for post in posts:
            if post.photo in photos:
                post.photo = url_for('uploaded_photo', photo=post.photo)

            #get username and user profile photo based on user id
            user_data = db.session.query(User.profile_photo, User.username) \
                        .join(Post, Post.user_id == User.id) \
                        .filter(Post.id == post.id) \
                        .first()
            
            profile_photo, username = user_data

            #get likes 
            likes = Like.query.filter_by(post_id=post.id).count()


            #did the current user like this?
            #TODO: fake user id
            fake_current_user = 1
            is_liked = Like.query.filter_by(post_id=post.id, user_id=fake_current_user).first()
            isLiked = bool(is_liked)
                        
            all_posts.append({
                "id": post.id,
                "profile_pic": "/uploads/" + profile_photo,
                "username": username,
                "photo": post.photo, #didn't do the route here because you got it before
                "caption": post.caption,
                "likes": likes,
                "isLiked": isLiked,
                "created_on": post.created_on

            })
        return jsonify(posts=all_posts), 200
    else:
        return jsonify(message="No posts found"), 200
    
@app.route('/api/v1/posts/<int:post_id>/like', methods=['POST'])
@requires_auth
def like_post(post_id):
    # Set a like on the current Post by the logged in User
    form = LikeForm(request.form, post_id=post_id)
    if form.validate_on_submit():
        current_user_id = g.current_user['sub']
        post_id = form.post_id.data

        post = Post.query.get(post_id)
        if not post:
            return jsonify({'error': 'Post not found'}), 400

        existing_like = Like.query.filter_by(post_id=post_id, user_id=current_user_id).first()
        if existing_like:
            return jsonify({'error': 'You have already liked this post', 'liked': True}), 200

        new_like = Like(post_id=post_id, user_id=current_user_id)
        db.session.add(new_like)
        db.session.commit()

        like_count = Like.query.filter_by(post_id=post_id).count()  # Assuming a simple count method for likes

        return jsonify({
            'message': 'You have liked the post',
            'liked': True,
            'like_count': like_count  # Update like count dynamically
        }), 201
    else:
        return jsonify(errors=form_errors(form)), 400

@app.route('/uploads/<photo>')
def uploaded_photo(photo):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), photo)

def get_uploaded_photos():
    rootdir = os.getcwd()
    image_list = []
    
    for subdir, dirs, files in os.walk(os.path.join(rootdir, app.config['UPLOAD_FOLDER'])):
        for file in files:
            if file.endswith(('.jpg', '.png', '.jpeg')):
                full_path = os.path.join(subdir, file)
                relative_path = os.path.relpath(full_path, os.path.join(rootdir, app.config['UPLOAD_FOLDER']))
                image_list.append(relative_path)
    return image_list


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

#TODO: uncomment

# @app.errorhandler(404)
# def page_not_found(error):
#     """Custom 404 page."""
#     return render_template('404.html'), 404