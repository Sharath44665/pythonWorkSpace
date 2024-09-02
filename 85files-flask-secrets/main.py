from flask import Flask, render_template, redirect
from createForms import MyForms
from flask_bootstrap import Bootstrap5

import os



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
bootstrap = Bootstrap5(app)

app.config['SECRET_KEY'] = os.urandom(32)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def loginPage():
    form = MyForms()

    # if form.validate_on_submit():
    #     return "success"
    if form.validate_on_submit():
        print(form.userEmail.data)
        useremail = form.userEmail.data
        userPasswd = form.password.data

        if useremail == "admin@email.com" and userPasswd == "12345678":
            return loginSuccess()

        return loginFail()

    return render_template("login.html", formData=form)


# @app.route("/loginSuccess")
def loginSuccess():
    return render_template("success.html")


def loginFail():
    return render_template("denied.html")


if __name__ == '__main__':
    app.run(debug=True)
