from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=url)
    response.raise_for_status()
    fakeBlogData = response.json()
    return render_template("index.html", fakeBlogData=fakeBlogData)

@app.route("/post/<pageNo>")
def redirectUrl(pageNo):
    blog = Post()
    blogData = blog.getData()[int(pageNo)-1]
    return render_template("post.html", blogData=blogData)


if __name__ == "__main__":
    app.run(debug=True)
