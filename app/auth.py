from flask import Blueprint, flash,render_template,redirect, request,url_for
from flask_login import UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db,login_manager
from app.models.user import User
auth = Blueprint('auth', __name__)
 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(Email=email).first()

        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not user.check_password(password):
            flash('Please check your login details and try again.','error')
            return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

            # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect(url_for('main.profile'))
    

    return render_template('login.html')

@auth.route('/signup',methods=["GET","POST"])
def signup():
    if request.method == "POST":
        # code to validate and add user to database goes here
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        id = request.form.get('id')
        # user = User.query.filter_by(email=email).first()
        existing_user = User.query.filter_by(Email = email).first()
        if existing_user: # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))
        
        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(StaffID=id,Email=email, StaffName=name, Password=generate_password_hash(password, method='pbkdf2',salt_length=256),Role='staff')

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully. You can now login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html')



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))