"""
HTTP logic only.
Parse input →
call DB/services →
return output
[ simple Flask routing basically ]
"""
from flask import Blueprint, render_template
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
