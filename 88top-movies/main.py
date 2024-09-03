from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float, desc
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from myform import Myform
from addform import AddForm
from getjson import getJsonData,getDataFromId

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String, nullable=True)
    img_url: Mapped[str] = mapped_column(String)


with app.app_context():
    db.create_all()



@app.route("/addToDB", methods=["GET", "POST"])
def add_to_db():
    if request.method == "GET":
        movieId = int(request.args.get("id"))
        getData = getDataFromId(movieId)
    # newMovie = Movie(
    #     title="Avatar The Way of Water",
    #     year=2022,
    #     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    #     rating=7.3,
    #     ranking=9,
    #     review="I liked the water.",
    #     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    #
    # )
        newMovie = Movie(
            title = getData["original_title"],
            year = int(getData["release_date"].split("-")[0]),
            description=getData["overview"],
            # rating=7.3,
            # ranking=9,
            # review="I liked the water.",
            img_url=f"https://image.tmdb.org/t/p/w500{getData['poster_path']}"

        )
        db.session.add(newMovie)
        db.session.commit()
        return redirect(url_for("updateRating", id=newMovie.id))

    return "something error in server"


@app.route("/add", methods=["POST", "GET"])
def addMovie():
    addform = AddForm()
    if addform.validate_on_submit():
        movieName = addform.name.data
        # print(movieName)
        jsonData = getJsonData(movieName)
        results = jsonData["results"]
        return render_template("select.html", results=results)

    return render_template("add.html", addform=addform)


@app.route("/delete", methods=["GET", "POST"])
def deleteRow():
    # print(request.args.get("id"))
    getId = request.args.get("id")
    deleteBook = db.get_or_404(Movie, getId)
    db.session.delete(deleteBook)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/edit", methods=["GET", "POST"])
def updateRating():
    myform = Myform()
    getId = request.args.get("id")
    updateRating = db.get_or_404(Movie, getId)

    if myform.validate_on_submit():
        updateRating.review = myform.reviewTextBox.data
        updateRating.rating = float(myform.ratingTextBox.data)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", myform=myform)


@app.route("/")
def home():
    # second_movie = Movie(
    #     title="Avatar The Way of Water",
    #     year=2022,
    #     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    #     rating=7.3,
    #     ranking=9,
    #     review="I liked the water.",
    #     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    # )
    # db.session.add(second_movie)
    # db.session.commit()

    # moviesList = db.session.execute(db.select(Movie).order_by(desc(Movie.ranking))).scalars()
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()  # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()


    return render_template("index.html", moviesList=all_movies)


if __name__ == '__main__':
    app.run(debug=True)
