"""
Parse input →
call DB/services →
return output as JSON
[ simple Flask routing basically + helper funcs ]
"""
from flask import Blueprint, flash, render_template, request, redirect, url_for, session
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

from .extensions import db, login_manager
from .models import User  # add others later (Cart, Orders, etc.)
from .forms import Login, Register

from datetime import date

bp = Blueprint('web', __name__)
