from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def getLogin():
    if request.method == "POST":
        username = request.form["name"]
        userPasswd = request.form["password"]

        return f"<h2>username: {username} Password: {userPasswd}</2>"
    return "login failed"

if __name__ == "__main__" :
    app.run(debug=True)




