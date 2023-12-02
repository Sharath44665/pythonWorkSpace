# import flask
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

loginManager = LoginManager()  # configuring the app
loginManager.init_app(app)  # initialising the loginManager


@loginManager.user_loader
def load_user(user_id):
    return db.get_or_404(User, ident=user_id)


# CREATE TABLE IN DB
class User(db.Model, UserMixin): # add this UserMixin to avoid this: AttributeError: 'User' object has
    # no attribute 'is_active'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in = current_user.is_authenticated)


def hashPasswdGenerate(userPasswd=None):
    return generate_password_hash(password=userPasswd, method="pbkdf2:sha256", salt_length=8)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        userName = request.form.get("name")
        userEmail = request.form.get("email")
        userPasswd = request.form.get("password")

        sqlQuery = db.session.execute(db.select(User).filter_by(email = userEmail))
        userInstance = sqlQuery.scalar()
        if userInstance:
            error= f"That email:{userEmail} is already used, please login"
            return render_template("login.html",error=error)

        # inserting into DB
        newUser = User(
            email = userEmail,
            password=hashPasswdGenerate(userPasswd=userPasswd),
            name=userName
        )
        db.session.add(newUser)
        db.session.commit()
        # return redirect(url_for("secrets"))
        login_user(newUser)  # Log in and authenticate user after adding details to database
        return render_template("secrets.html", name=userName)

    return render_template("register.html", logged_in= current_user.is_authenticated)


# def userPasswordCheck(userPasswd=None, dbPassword=None):
#     print(check_password_hash(pwhash=dbPassword, password=userPasswd ))

@app.route('/login', methods=["GET", "POST"])
def login():
    loginUsername = request.form.get("email")
    loginPasswd = request.form.get("password")

    if request.method == "POST":

        # userInstance = db.get_or_404(User, loginUsername )
        val = db.query.Query(User).filter_by(email=loginUsername)
        dbUser = db.session.execute(val)
        userInstance = dbUser.scalar()

        # userPasswordCheck(userPasswd=loginPasswd, dbPassword=userInstance.password)

        if userInstance is None:
            error = "Email Not Exist"
            return render_template("login.html",error=error)
        elif check_password_hash(userInstance.password, loginPasswd) is False:
            error = "incorrect password"
            return render_template("login.html",error=error)
        elif check_password_hash(userInstance.password, loginPasswd):
            flash('Logged in successfully.')
            login_user(userInstance)  # Log in and authenticate user after adding details to database
            return redirect(url_for('secrets'))

    return render_template("login.html", logged_in=current_user.is_authenticated)


# Only logged-in users can access the route
@app.route('/secrets')
@login_required
def secrets():
    # querying the data using ORDER by DESC with limit
    # userDB = db.session.execute(db.select(User).order_by(id))
    # userQuerry = User.query.order_by(User.id.desc()).limit(1)
    # dbVal = db.session.execute(statement=userQuerry)
    # lastUser = dbVal.scalars().all()
    #
    # return render_template("secrets.html" , dbData= lastUser[0])
    print(current_user.name)
    return render_template("secrets.html", name = current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return render_template("index.html")


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory="static", path="files/cheat_sheet.pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)
