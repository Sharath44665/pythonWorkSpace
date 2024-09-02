from flask import Flask, render_template
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import InputRequired, ValidationError


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap4(app)

def custom_validator(roughForm, field):
    if len(field.data) < 8:
        raise ValidationError("less than 8, enter more ")
class MyForm(FlaskForm):
    my_field = StringField('My Field', validators=[validators.InputRequired(),custom_validator])
    submit = SubmitField(label="Enter")


# def my_length_check( form, name):
#     print(name.data)
#     if len(name.data) < 8:
#         raise ValidationError('Field must be greater than 8 characters')
#
# class MyForm(FlaskForm):
#     name = StringField(label="Name", validators=[InputRequired(),my_length_check])
#     submit = SubmitField(label="Enter")



@app.route("/")
def helloPage():
    return "Hello"

@app.route("/rough", methods=["GET","POST"])
def roughWork():
    roughForm = MyForm()
    if roughForm.validate_on_submit():
        s = roughForm.my_field.data
        print(s)
    else:
        print(roughForm.form_errors)

    return render_template("rough.html", roughForm=roughForm)



if __name__ == "__main__":
    app.run(debug=True)
