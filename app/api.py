"""
HTTP logic only.
Parse input →
call DB/services →
return output
[ simple Flask routing basically ]
"""
from flask import Blueprint, flash, render_template, request, redirect, url_for
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

from .extensions import db, login_manager
from .models import User  # add others later (Cart, Orders, etc.)
from .forms import Login, Register

from datetime import date

bp = Blueprint('api', __name__)

@bp.route("/")
def index():
    year = date.today().year
    return render_template("index.html", year=year)

@bp.route("/products")
def products():
    return render_template("products.html")

@bp.route("/error")
def error():
    return render_template("404.html")

@bp.route("/login", methods=["GET", "POST"])
def login():

    form=Login()
    if form.validate_on_submit():
        password = form.password.data
        result = db.session.execute(db.select(User).where(User.username == form.username.data))
        user = result.scalar()
        if not user:
            flash("That username does not exist, please try again.")
            return redirect(url_for('api.login'))
        elif not check_password_hash(user.password_hash, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('api.login'))
        else:
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('api.index'))
    return render_template("login.html", form=form)

@bp.route("/register", methods=["GET", "POST"])
def register():
    error = None
    form = Register()
    if form.validate_on_submit():

        password = form.password.data
        r_pass = form.r_password.data

        new_user = User(username=form.username.data,
                        email=form.email.data,
                        password_hash=generate_password_hash(password),
                        created_at=date.today().strftime("%B %d, %Y")
        )

        db.session.add(new_user)
        db.session.commit()

        if password == r_pass:
            return redirect(url_for('api.index'))
        else:
            error = 'passwords must be identical'

    return render_template("signup.html", form=form, error=error)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('api.login'))

@bp.route("/features")
def features():
    return render_template("features.html")

@bp.route("/about")
def about():
    return render_template("about.html")