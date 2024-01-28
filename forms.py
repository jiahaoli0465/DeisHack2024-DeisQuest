from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, TextAreaField, validators, SelectField, FormField, IntegerField, FloatField, SelectMultipleField
from wtforms.validators import InputRequired, Email, Optional, Length

class RegisterForm(FlaskForm):
    """Form for registering a user."""


    email = EmailField("Email", validators=[InputRequired(), Email()])
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])



class LoginForm(FlaskForm):
    """Form for logging in a user."""

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])



