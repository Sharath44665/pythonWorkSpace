from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! Hello Sharath...</p>"

@app.route("/bye")
def sayBye():
    return "<h4>Bye...</h4>"

@app.route("/<name>/<path:subpath>/<int:num>") # url/name/12/23
def greet(name,subpath,num):
    return f"<h3>Hi {name}!!</h3><p>You are {subpath} years old {num}</p>"

if __name__ == "__main__":
    app.run(debug=True)

