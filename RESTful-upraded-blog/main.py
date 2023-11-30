from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from wtforms import ValidationError

from createForms import CreateBlogForm,RoughPostForm
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

''' 
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()

# rough work
@app.route("/rough")
def roughWork():
    roughForm = RoughPostForm()
    return render_template("rough.html", form=roughForm)



@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []
    getAllFromDB = db.session.execute(db.select(BlogPost))
    posts = getAllFromDB.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.

@app.route('/show_post/<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = "Grab the post from your database"
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


def getDate():
    x = date.today()
    newDate = x.strftime("%B %d, %Y")
    return newDate


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["POST", "GET"])
def add_new_post():
    makeBlogForm = CreateBlogForm()

    # if request.method == "POST":
    #     if len(request.form.get('ckeditor')) == 0:
    #         request.method = False
    #         raise ValidationError("Blog content Should not be empty.")

    if request.method == "POST" and makeBlogForm.validate_on_submit():
        print(makeBlogForm.blogPostTitle.data)

        newBlogPost = BlogPost(
            title=makeBlogForm.blogPostTitle.data,
            subtitle=makeBlogForm.subTitle.data,
            date=getDate(),
            body= makeBlogForm.blogArea.data,
            author=makeBlogForm.yourName.data,
            img_url=makeBlogForm.imgUrl.data

        )
        db.session.add(newBlogPost)
        db.session.commit()
        print("successfully done")
        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form=makeBlogForm)


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<post_id>", methods=["GET","POST"])
def editPost(post_id):
    updateDB = db.get_or_404(BlogPost,post_id)
    newForm = CreateBlogForm(
        blogPostTitle = updateDB.title,
        subTitle = updateDB.subtitle,
        yourName = updateDB.author,
        imgUrl = updateDB.img_url,
        blogArea = updateDB.body

    )

    if request.method == "POST" and newForm.validate_on_submit():
        updateDB.title = newForm.blogPostTitle.data
        # db.session.commit()
        updateDB.subtitle = newForm.subTitle.data
        # db.session.commit()
        updateDB.date = getDate()
        # db.session.commit()
        updateDB.body = newForm.blogArea.data
        # db.session.commit()
        updateDB.author = newForm.yourName.data
        # db.session.commit()
        updateDB.img_url = newForm.imgUrl.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=updateDB.id))


    return render_template('make-post.html', form=newForm)
    # return redirect(url_for('add_new_post'))


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete-post/<post_id>")
def delete_post(post_id):
    deleteDB = db.get_or_404(BlogPost,post_id)
    db.session.delete(deleteDB)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
