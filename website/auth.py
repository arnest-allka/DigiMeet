from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models.user import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.get_by_username(username)
        if user:
            if check_password_hash(user.password_hash, password):            
                login_user(user, remember=True)
                flash('Logged in successfully!', category='success')
                return redirect(url_for('routes.home'))
            else:
                flash('Wrong password', category='error')                
        else:
            flash('User does not exist', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if User.get_by_username(username):
            flash('Username already exists. Choose a different one.', category='error')
        elif User.get_by_email(email):
            flash('Email already exists. Choose a different one.', category='error')
        elif not all((email, first_name, last_name, username, password1, password2)):
            flash("Missing fields", category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=generate_password_hash(password1))
            new_user.save_to_db()
            flash('Registration successful. You can now log in.', category='success')
            return redirect(url_for('auth.login'))

    return render_template("register.html", user=current_user)
