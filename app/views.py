"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, jsonify, send_file
import os
from app.models import User, Like, Follow
from app.forms import RegisterForm, LoginForm
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

app.config['WTF_CSRF_ENABLED'] = False #Comment out
@app.route('/api/v1/register', methods=['POST'])
def register():
    form = RegisterForm()  
    if form.validate():  
        username = form.username.data
        password = form.password.data
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        location = form.location.data
        biography = form.biography.data
        """profile_photo = form.profile_photo.data
        
        # Save profile photo
        filename = secure_filename(profile_photo.filename)
        profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))"""
        
        new_user = User(
            username=username,
            password=password,
            firstname=firstname,
            lastname=lastname,
            email=email,
            location=location,
            biography=biography
            #profile_photo = filename
        )
        
        db.session.add(new_user)
        db.session.commit() 
        
        return jsonify({"message": "User registered successfully"}), 200
    else:
        errors = form.errors 
        C


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is not None and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return jsonify({"message": "User logged in successfully"}), 200
        else:
            #flash('Invalid username or password', 'danger')
            return jsonify({"message": "User registered successfully"}), 200

@app.route(("/logout"))
@login_required
def logout():
    logout_user()
    flash('Logout successful!', 'success')
    return redirect(url_for("home"))
    
# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(UserProfile).filter_by(id=id)).scalar()


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