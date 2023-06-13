from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = TextAreaField("Title", validators=[DataRequired()])
    content = TextAreaField("Text", validators=[DataRequired()])
    submit = SubmitField("Post")

    

