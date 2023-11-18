from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("index.html")

# edit directly on web page
# open developer tools -> console:






