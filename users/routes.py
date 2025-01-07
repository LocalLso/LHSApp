from flask import Blueprint, render_template, redirect, url_for, request, session
from extensions import db, login_manager
from users.models import User
from users.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

users_bp = Blueprint('users', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@users_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('assessments.dashboard'))
    return render_template('index.html')

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('assessments.dashboard'))
        return 'Invalid username or password'
    return render_template('login.html', form=form)

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)

@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.index'))

