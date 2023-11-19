from flask import Flask,render_template
import random,datetime
from getDataAPI import getDataFromAPI,getGender

app = Flask(__name__)


@app.route("/")
def homePage():

    randomNo = random.randint(0,100)
    now = datetime.datetime.now()
    year = now.year
    userName = "Sharatchandra"
    return render_template("index.html", randomNum=randomNo, currentYear=year, userName=userName)

@app.route("/<userName>")
def userPage(userName):
    jsonData = getDataFromAPI(userName)
    genderData = getGender(userName)
    return render_template("userName.html", userTitle=jsonData["name"],
                           userName=jsonData["name"].title(),
                           ageNo=jsonData["age"], gender= genderData["gender"] )
if __name__ == "__main__":
    app.run(debug=True)

