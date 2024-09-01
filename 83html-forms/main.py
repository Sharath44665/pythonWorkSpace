from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def goHomePage():
    return  render_template("index.html")

@app.route("/login", methods =["GET","POST"])
def recieveData():
    if request.method == 'POST':
                            # print(request.form) # ImmutableMultiDict([('user', 'Sharath')])
                            # print(request.form['user']) # Sharath
        username = request.form['user']
        userPasswd = request.form['pass']
        return render_template("loginSuccess.html", name= username, passwd=userPasswd)

    else:
        print("not working")
    pass


if __name__ == "__main__":
    app.run(debug=True)