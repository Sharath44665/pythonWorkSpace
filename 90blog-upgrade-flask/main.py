import requests
from flask import Flask, render_template, request, url_for, redirect
from jinja2 import TemplateNotFound

from post import Post
from datetime import date, timedelta
import random

app = Flask(__name__)
posts = Post()

randomDates = {}

startDate = date(2023, 1, 1)
endDate = date(2023, 12, 31)


@app.route("/")
def homepage():
    myPost = posts.getData()

    for idx in range(3):
        randomDate = generateRandomDate(startDate, endDate)
        randomDates[idx] = f"{randomDate}"
    print(randomDates)

    return render_template("index.html", myPost=myPost, randomDates=randomDates)


# generating random date
def generateRandomDate(startDate, endDate):
    days = (endDate - startDate).days
    randomDay = random.randrange(days)
    return startDate + timedelta(days=randomDay)


@app.route("/post/<pageVal>", methods=['POST', 'GET'])
def makePost(pageVal):
    myPost = posts.getData()
    myPost = myPost[int(pageVal) - 1]
    # print(setDate)
    # print(request.args['setDate'])
    setDate = request.args['setDate']

    return render_template("post.html", myPost=myPost, setDate=setDate)


@app.route("/about")
def aboutPage():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contactPage():
    if request.method == "POST":
        username = request.form["username"]
        usermail = request.form["email"]
        phoneNum = request.form["phone"]
        userMsg = request.form["message"]

        contactData = {
            "username": username,
            "email": usermail,
            "phone": phoneNum,
            "message": userMsg
        }
        try:
            posts.sendMailToUser(contactData=contactData)
        except FileNotFoundError:
            print("file not found  render to somewhere")
            return redirect(url_for('fileNotFoundError'))
        # except TemplateNotFound:
        #     return render_template('fileNotFoundError')

        # print(f"username: {username}, email: {usermail}, phone: {phoneNum}, msg: {userMsg}")

    return render_template("contact.html")


@app.route("/fileNotFound")
def fileNotFoundError():
    return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)
