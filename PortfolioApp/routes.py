from PortfolioApp import app
from flask import render_template
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator

app.config.update(dict(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'ridamansy',
    MAIL_PASSWORD = '[password]'
))

mail = Mail(app)



@app.route('/')
@app.route('/home', methods=["GET", "POST"])
def home():
    cform = contactForm()
    return render_template('index.html', form=cform)


class contactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[
    DataRequired(), Email(granular_message=True)])
    message= StringField(label='Message')
    submit = SubmitField(label="Submit")
