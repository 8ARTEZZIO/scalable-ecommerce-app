"""
store all the Flask-WTF forms
"""

from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.numeric import IntegerField, FloatField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, Length, Email, URL


class Register(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(3, 40, message="Username must be at least 3 characters long")])
    email = StringField('Email address', validators=[DataRequired(), Email(message="Provide correct email")])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 40, message="Password must be at least 8 characters long")])
    r_password = PasswordField('Repeat Password', validators=[DataRequired()])
    submit = SubmitField('Sign up')

class Login(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(3, 40, message="Username must be at least 3 characters long")])
    password = PasswordField(validators=[DataRequired(), Length(8, 40)])
    submit = SubmitField('Log In')

class AddProduct(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    slug = StringField('Slug', validators=[URL()])
    price = FloatField(validators=[DataRequired()])
    currency = StringField(default='USD', validators=[Length(min=3, max=3)])
    stock = IntegerField()
    image_url = StringField('Image URL', validators=[URL()])
    description = StringField('description', validators=[DataRequired()])
    active = BooleanField()
    submit = SubmitField('Add Product')