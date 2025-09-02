"""
HTTP logic only.
Parse input →
call DB/services →
return output
[ simple Flask routing basically ]
"""
from flask import Blueprint, flash, render_template, request, redirect, url_for
from .forms import *
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

@bp.route("/login")
def login():

    form=Login()
    return render_template("login.html", form=form)

@bp.route("/register", methods=["GET", "POST"])
def register():
    error = None
    form = Register()
    if form.validate_on_submit():

        username = form.username.data
        email = form.email.data
        password = form.password.data
        r_pass = form.r_password.data

        if password == r_pass:
            return redirect(url_for('api.index'))
        else:
            error = 'passwords must be identical'

    return render_template("signup.html", form=form, error=error)