from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    name = StringField(label='Movie Name', validators=[DataRequired()])
    submitButton = SubmitField(name="Add")

