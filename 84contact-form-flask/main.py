from flask import Flask, render_template,request
import requests,smtplib, pandas

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",methods=['POST','GET'])
def contact():

    myData = pandas.read_csv("./token.csv")
    senderEmail = myData["sender"].get(0)
    appPasswd = myData["app_passwd"].get(0)
    messageSent = False
    if request.method == "POST":
            # print(request.form["name"])
            # print(request.form["email"])
            # print(request.form["phone"])
            # print(request.form["message"])

            userName = request.form["name"]
            userEmail = request.form["email"]
            subject = "Subject: Email From Blog"
            blogMsg=request.form["message"]
            userMsg = f"{subject}\n\nUserName: {userName}\n{blogMsg}"

            with smtplib.SMTP(host="smtp.gmail.com", port=587) as myConnection:
                myConnection.starttls()
                myConnection.login(user=senderEmail, password=appPasswd)
                myConnection.sendmail(from_addr=senderEmail, to_addrs=userEmail, msg=userMsg)
            messageSent = True
            # return render_template("contactSuccess.html")
            return render_template("contact.html", messageSent=messageSent)

    return render_template("contact.html", messageSent=messageSent)


# noinspection PyPackageRequirements
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
