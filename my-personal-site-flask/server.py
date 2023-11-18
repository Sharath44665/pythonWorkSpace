from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return render_template("index.html")

@app.route("/demo")
def displayProfile():
    return render_template("demoSite.html")

if __name__ == "__main__":
    app.run(debug=True)


