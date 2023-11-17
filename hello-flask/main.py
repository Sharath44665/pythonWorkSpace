from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! Hello Sharath...</p>"

@app.route("/bye")
def sayBye():
    return "<h4>Bye...</h4>"