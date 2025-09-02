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

from .extensions import db
from .models import Users, Products  # add others later (Cart, Orders, etc.)
from .forms import Login, Register

import datetime

bp = Blueprint('api', __name__)

@bp.route("/")
def index():
    year = datetime.date.today().year
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
    return render_template("login.html", form=form)

@bp.route("/register", methods=["GET", "POST"])
def register():
    error = None
    form = Register()
    if form.validate_on_submit():

        new_user = Users
        username = form.username.data
        email = form.email.data
        password = form.password.data
        r_pass = form.r_password.data

        if password == r_pass:
            return redirect(url_for('api.index'))
        else:
            error = 'passwords must be identical'

    return render_template("signup.html", form=form, error=error)

@bp.route("/logout", methods=["POST", "GET"])
def logout():

    return render_template("index.html")