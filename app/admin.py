from flask import Blueprint, flash, render_template, request, redirect, url_for, session, jsonify
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

from .extensions import db, login_manager
from .models import User, Product  # add others later (Cart, Orders, etc.)
from .forms import Login, Register, AddProduct

from datetime import date

bp = Blueprint('admin', __name__)

@bp.route("/admin/products", methods=["GET"])
def admin_products():
    return render_template("products.html")

@bp.route("/admin/products/add", methods=["GET", "POST"])
def admin_add_product():
    return render_template("add_product.html")

@bp.route("/admin/products/<int:id>/edit", methods=["GET", "POST"])
def admin_edit_product(id):
    return render_template("products.html")

@bp.route("/admin/products/<int:id>/delete", methods=["POST"])
def admin_del_product(id):
    render_template("products.html")