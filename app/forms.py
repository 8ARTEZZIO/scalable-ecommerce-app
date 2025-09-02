"""
store all the Flask-WTF forms
"""

from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email


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