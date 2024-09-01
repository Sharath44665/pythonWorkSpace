from flask import Flask, render_template
from datetime import datetime, timedelta
import requests

app = Flask(__name__)

@app.route("/")
def homePage():
    jsonData = getJasonData()
    dateList = getDateList()
    return render_template("index.html", allPost =jsonData, diffDates = dateList)

@app.route("/about")
def aboutPage():
    return render_template("about.html")

@app.route("/contact")
def contactPage():
    return  render_template("contact.html")

@app.route("/post")
def makePost():
    return render_template("post.html",  allPosts=None, postNo=0, diffDates = None)

@app.route("/post/<postNo>")
def postPage(postNo):
    jsonData = getJasonData()
    dateList = getDateList()
    return render_template("post.html", allPosts=jsonData, postNo=int(postNo), diffDates = dateList)

def getJasonData():
    url = "https://api.npoint.io/674f5423f73deab1e9a7"
    response = requests.get(url)
    response.raise_for_status()
    jsonData = response.json()
    return jsonData

def getDateList():
    dateList = []
    dateList.append(getDates(30))
    dateList.append(getDates(45))
    dateList.append(getDates(60))
    return dateList
def getDates(diff):
    nowDate = datetime.now()
    # daysToSubtract = diff
    timeDateDiff = timedelta(days=diff)
    newDiffDate = nowDate - timeDateDiff
    return newDiffDate.date()

if __name__ == "__main__":
    app.run(debug=True)