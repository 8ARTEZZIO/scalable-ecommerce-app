"""
HTTP logic only.
Parse input →
call DB/services →
return output
[ simple Flask routing basically ]
"""
from flask import Flask, render_template, Blueprint
import datetime

bp = Blueprint('api', __name__)
app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    year = datetime.date.today().year
    return render_template("index.html", year=year)

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/error")
def error():
    return render_template("404.html")

if __name__ == "__main__":
    app.run(port=5050, debug=True)