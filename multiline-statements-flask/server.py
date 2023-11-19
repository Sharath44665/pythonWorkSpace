
from flask import Flask, render_template
import requests,random

app = Flask(__name__)

@app.route("/")
def displayHome():
    userName = "Sharathchandra"
    n = random.randint(0,100)
    return render_template("index.html", username=userName, num=n)


@app.route("/blog/<printNumTerminal>")
def blogPost(printNumTerminal):
    print(printNumTerminal)
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=url)
    response.raise_for_status()
    blogData = response.json()

    return render_template("blog.html", blogData=blogData)



if __name__ == "__main__":
    app.run(debug=True)

