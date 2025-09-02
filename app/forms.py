"""
store all the Flask-WTF forms
"""

from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class Register(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(3, 40)])
    email = StringField('Email address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    r_password = PasswordField('Repeat Password', validators=[DataRequired()])
    submit = SubmitField('Sign up')

class Login(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(3, 40)])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Log In')