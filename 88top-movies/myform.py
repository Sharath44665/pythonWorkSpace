from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Myform(FlaskForm):
    ratingTextBox = StringField(label= "Change the rating Out of 10, e.g. 7.5", validators= [DataRequired()])
    reviewTextBox = StringField(label="Your Review", validators=[DataRequired()])
    submitButton = SubmitField(label="Update Values")



