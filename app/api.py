"""
Parse input →
call DB/services →
return output as JSON
[ simple Flask routing basically + helper funcs ]
"""
from flask import Blueprint, flash, render_template, request, redirect, url_for, session, jsonify
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

from .extensions import db, login_manager
from .models import User, Product  # add others later (Cart, Orders, etc.)
from .forms import Login, Register, AddProduct

from datetime import date

bp = Blueprint('api', __name__)

# @bp.route("/api/get_prod_data", methods=["GET"])
# def get_prod_data():
