from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo, Regexp
class PostForm(FlaskForm):
    title = TextAreaField("Title", validators=[DataRequired()])
    content = TextAreaField("Text", validators=[DataRequired()])
    submit = SubmitField("Post")

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

