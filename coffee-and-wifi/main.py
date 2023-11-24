from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,URLField,validators,SelectField
from wtforms.validators import DataRequired, URL,InputRequired
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


def check_am_pm(form, field):
    val = field.data.strip().lower()[-2:]
    # print(val)
    if val != "pm" and val != "am":
        raise validators.ValidationError("Please enter AM or PM ")




class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField(label="Locatioins", validators = [DataRequired(),URL(require_tld=True, message=None)])
    openCafe = StringField(label="Open Time", validators=[InputRequired(),check_am_pm])
    closeCafe = StringField(label="Closing Time", validators=[InputRequired(),check_am_pm])
    coffee = SelectField(label= "Select coffee", choices=[("✖️"),("☕☕☕☕☕"),("☕☕☕☕"),("☕☕☕"),("☕☕"),("☕")])
    wifi = SelectField(label="Wifi Raing", choices=[("✖️"),("💪💪💪💪💪"),("💪💪💪💪"),("💪💪💪"),("💪💪"),("💪")])
    powerConnect = SelectField(label= "Power connector", choices=[("✖️"),("🔌🔌🔌🔌🔌"),("🔌🔌🔌🔌"), ("🔌🔌🔌"),("🔌🔌"),("🔌")])
    submit = SubmitField('Submit')



# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["GET","POST"])
def add_cafe():
    form = CafeForm()


    if form.validate_on_submit():
        formData = [[form.cafe.data, form.location.data, form.openCafe.data, form.closeCafe.data, form.coffee.data,
                     form.wifi.data, form.powerConnect.data]]

        with open(file="cafe-data.csv",mode="a") as myFile:
            csvWrite = csv.writer(myFile)
            csvWrite.writerows(formData)

        return cafes()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():

    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
