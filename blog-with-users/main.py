from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
# from flask_gravatar import Gravatar # not working
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm

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
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Configure Flask-Login
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(Users, ident=user_id)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)
login_manager.init_app(app)

# gravatar = Gravatar(app,
#                     size=100,
#                     rating='g',
#                     default='retro',
#                     force_default=False,
#                     force_lower=False,
#                     use_ssl=False,
#                     base_url=None)
# CONFIGURE TABLES

# TODO: Create a User table for all your registered users. 
class Users(db.Model, UserMixin):
    __tablename__ ="users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    userEmail = db.Column(db.String(250),nullable=False, unique=True)
    password = db.Column(db.String(250),nullable=False)

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    img_url = db.Column(db.String(250), nullable=False)

class Comments(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    comment_body = db.Column(db.Text, nullable = False)
    post_id = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    users = db.relationship("Users",backref=db.backref('comments',lazy=True))

with app.app_context():
    db.create_all()


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register',methods=["GET","POST"])
def register():
    registerForm = RegisterForm()
    if request.method == "POST" and registerForm.validate_on_submit():
        formEmail = registerForm.email.data
        formUser = registerForm.name.data
        password = generate_password_hash(registerForm.password.data, method="pbkdf2", salt_length=8)

        queryData = db.session.execute(db.select(Users).filter_by(userEmail=formEmail))
        userInstance = queryData.scalar()
        if userInstance is None:
            newUser= Users(
                username= formUser,
                userEmail= formEmail,
                password = password
            )
            db.session.add(newUser)
            db.session.commit()
            login_user(newUser)
            return redirect(url_for('get_all_posts'))
            # return render_template("index.html", current_user=current_user)
        elif userInstance:
            flash(f"{formEmail} already exists, please Login")
            return redirect(url_for("login"))
    return render_template("register.html", form= registerForm)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=["GET", "POST"])
def login():
    loginForm= LoginForm()
    if request.method == "POST" and loginForm.validate_on_submit():

        formEmail = loginForm.email.data
        formPasswd = loginForm.password.data

        dbQuery = db.session.execute(db.select(Users).filter_by(userEmail=formEmail))
        userInstance = dbQuery.scalar()

        if userInstance is None:
            flash(f"{formEmail} not found in our database")
            # print("email is not valid")
            return redirect(url_for("register"))
        elif check_password_hash(userInstance.password, formPasswd) is False:
            flash("password incorrect")
            # print("passwd is not valid")
        elif userInstance.userEmail == formEmail and check_password_hash(userInstance.password, formPasswd):
            # print(userInstance)
            login_user(userInstance)
            # print("success")
            return redirect(url_for("get_all_posts"))


    return render_template("login.html", form=loginForm)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


# home page
@app.route('/')
def get_all_posts():
    if not current_user.is_authenticated: # user is not signed in
        result = db.session.execute(db.select(BlogPost))
        posts = result.scalars().all()

    if current_user.is_authenticated and current_user.id > 2: # those users who wants to sign in as customers
        result = db.session.execute(db.select(BlogPost))
        posts = result.scalars().all()

    if current_user.is_authenticated and current_user.id <=2: # user having admin, can do new post, delete post, or edit post
        # print("home page: {fcurrent_user.username}")
        queryData = db.session.execute(db.select(BlogPost).filter_by(author=current_user.username))
        result = queryData.scalars().all()
        posts = result
        pass
    # current_user = login_user()
    return render_template("index.html", all_posts=posts)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET","POST"])
def show_post(post_id):
    commentForm = CommentForm()
    queryData = db.session.execute(db.select(Comments, Users).join(Comments.users).where(Comments.post_id==post_id))
    allData = queryData.fetchall()

    # for comment, user in allData:
    #     print(f"{comment.comment_body}, {user.username}")
    # print(allData)
    if commentForm.validate_on_submit():
        if not current_user.is_authenticated:
            flash("Please login First, Then comment")
        elif current_user.is_authenticated:
            newComment = Comments(
                comment_body = commentForm.commentBody.data,
                author_id = current_user.id,
                post_id = post_id
            )
            db.session.add(newComment)
            db.session.commit()

            pass
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post, form = commentForm, allData= allData)


# TODO: Use a decorator so only an admin user can create a new post

def admin_required(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        # print(f"admin_required: {current_user.is_authenticated}")
        try:
            if current_user.id > 2:
                return abort(404)
        except AttributeError:
            return abort(404)
        return function(*args, **kwargs)
    return decorated_function # dont forget to remove parenthesis
# def admin_only(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         #If id is not 1 then return abort with 403 error
#         if current_user.id != 1:
#             return abort(403)
#         #Otherwise continue with the route function
#         return f(*args, **kwargs)
#     return decorated_function

@app.route("/new-post", methods=["GET", "POST"])
@admin_required
# @login_required
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user.username,
            author_id = current_user.id,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_required
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post

@app.route("/delete/<int:post_id>")
@admin_required
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
