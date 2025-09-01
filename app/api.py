"""
HTTP logic only.
Parse input →
call DB/services →
return output
[ simple Flask routing basically ]
"""
from flask import Blueprint, render_template, request, redirect, url_for
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
    return render_template("login.html")

@bp.route("/register", methods=["GET", "POST"])
def register():

    form = Register()
    if form.validate_on_submit():
        username = form.username
        print(username)


    return render_template("signup.html", form=form)