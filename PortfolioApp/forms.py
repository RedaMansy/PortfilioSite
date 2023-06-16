from typing import Text
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo, Regexp
class PostForm(FlaskForm):
    title = CKEditorField("Title", validators=[DataRequired()])
    content = CKEditorField("Text", validators=[DataRequired()])
    submit = SubmitField("Post")

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

