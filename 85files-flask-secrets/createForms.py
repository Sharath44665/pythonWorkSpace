from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email,Length


class MyForms(FlaskForm):
    userEmail = EmailField(label='user email: ', validators=[Email(message=None, granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
    password = PasswordField(label="Password: ", validators=[Length(min=8)])
    submit = SubmitField(label="Login")
