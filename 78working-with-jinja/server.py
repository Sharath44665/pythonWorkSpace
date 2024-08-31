from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def goHome():
    myList = ["sharath", "john", "kennedy"]

    thisYear = datetime.now().year
    myList[0] = thisYear
    return render_template("index.html", userList=myList)

if __name__ == "__main__":
    app.run(debug=True)

