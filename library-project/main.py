from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
all_books = []


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book = Book(
            title=request.form["book-name"],
            author=request.form["book-author"],
            rating=float(request.form["rating"])

        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html")


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book)).scalars()
    all_books = list(all_books.all())



    return render_template("index.html", books=all_books)


@app.route("/edit", methods=["GET", "POST"])
def editRating():
    with app.app_context():
        editBook = db.session.execute(db.select(Book).where(Book.id == request.args.get("id"))).scalar()
        if request.method == "POST":
            editBook.rating = float(request.form["changeRating"])
            db.session.commit()
            return redirect(url_for('home'))

    return render_template("edit.html", editBook=editBook)

@app.route("/delete", methods=["GET","POST"])
def deleteRow():

    if request.method == "GET":
        # print(request.args.get("id"))
        with app.app_context():
            bookDelete = db.session.execute(db.select(Book).where(Book.id == request.args.get("id"))).scalar()
            db.session.delete(bookDelete)
            db.session.commit()
            return redirect(url_for('home'))

    # return render_template("index.html")
    return redirect(url_for('home'))





if __name__ == "__main__":
    app.run(debug=True)
