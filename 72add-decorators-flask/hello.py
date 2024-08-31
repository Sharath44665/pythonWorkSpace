from flask import Flask

app = Flask(__name__)

def makeBold(function):
    def wrapperFunction():
        return f"<h2>{function()}</h2>"
    return wrapperFunction

def makeItalics(function):
    def wrapperFun():
        return f"<em>{function()}</em>"
    return wrapperFun

def makeUnderLine(function):
    def wrapperFun():
        return f"<u>{function()}</u>"
    return wrapperFun


@app.route("/")
@makeUnderLine
def hello_world():
    return "<p>Hello, World!</p>"



@app.route("/bye")
@makeBold
@makeItalics
@makeUnderLine
def bye():
    return "Bye"


if __name__ == "__main__":
    app.run(debug=True)
