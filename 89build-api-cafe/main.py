import sqlalchemy
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

# creating api using postman.
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


# making delete on api with user api key
@app.route("/report-closed/<id>", methods=["DELETE"])
def deleteDBWithKey(id):
    # print(request.args.get("api_key"))

    userAPIKey = request.args.get("api_key")
    userAuthKey = "TopSecretKey"
    newID = int(id)

    if userAPIKey == userAuthKey:
        try:
            val = db.session.execute(db.select(Cafe).filter_by(id=newID)).scalar_one()
        except sqlalchemy.exc.NoResultFound:

            msg= {"not found": "id not exist in the database"}
            return jsonify(response=msg)
        else:
            deleteCafe =db.get_or_404(Cafe,newID)
            db.session.delete(deleteCafe)
            db.session.commit()
            msg = {"deleted": "successfully deleted"}
            return jsonify(response=msg)
    else:
        msg={"fail": "api key not found"}
        return jsonify(response=msg),404



# making a patch, meaning updating something
@app.route("/update-price/<id>", methods=["PATCH"])
def udpatePriceInDB(id):
    try:
        # this code is to throw exception so that we can print error code
        if request.method == "PATCH":
            # print(id)
            newid = int(id)
            checkCafe = db.session.execute(db.select(Cafe).filter_by(id=newid)).scalar_one()
    except sqlalchemy.exc.NoResultFound:
        return jsonify(response={"fail": "id not found"}), 404

    updateCafe = db.get_or_404(Cafe, int(id))
    if updateCafe:

        updateCafe.coffee_price = f"£{request.args.get('new_price')}"
        db.session.commit()

        jsonMsg = {"success": "Successfully updated the price"}
        return jsonify(response=jsonMsg)


# make a post in api
#
@app.route("/add", methods=["POST"])
def dbAddRecords():
    newCafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=f"£{request.form.get('coffee_price')}"
    )
    db.session.add(newCafe)
    db.session.commit()
    val = {"success": "Successfully added the new cafe"}
    return jsonify(response=val)


# make api and search value
@app.route("/search", methods=["GET"])
def searchDB():
    if request.method == "GET":
        loc = request.args.get("loc").title()

    pattern = f"%{loc}%"
    results = db.session.execute(db.select(Cafe).filter(Cafe.location.like(pattern)))
    dbResult = results.scalars().all()
    if len(dbResult) == 0:
        error = {
            "Not Found": "Sorry, we dont have a cafe at that location"
        }
        return jsonify(error=error), 404
    filterVal = {}
    for row in dbResult:
        filterVal[row.id] = {
            "name": row.name,
            "map_url": row.map_url,
            "img_url": row.img_url,
            "location": row.location,
            "seats": row.seats,
            "has_toilet": row.has_toilet,
            "has_wifi": row.has_wifi,
            "has_sockets": row.has_sockets,
            "can_take_calls": row.can_take_calls,
            "coffee_price": row.coffee_price
        }

    return jsonify(results=filterVal)


# @app.route("/all")
# def get_all_cafes():
#     result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
#     all_cafes = result.scalars().all()
#     # for val in all_cafes:
#     #     print(val.to_dict()) # database object is not converting into dictionary
#     # This uses a List Comprehension but you could also split it into 3 lines.
#     return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes]) # database object is not converting into dictionary

# make api and send all value
@app.route("/all")
def getAllFromDB():
    allCafes = db.session.execute(db.select(Cafe))
    # allCafes = list(allCafes.scalars().all())
    allCafes = allCafes.scalars().all()
    result = {}
    for idx in range(len(allCafes)):
        result[idx] = {

            "name": allCafes[idx].name,
            "map_url": allCafes[idx].map_url,
            "img_url": allCafes[idx].img_url,
            "location": allCafes[idx].location,
            "seats": allCafes[idx].seats,
            "has_toilet": allCafes[idx].has_toilet,
            "has_wifi": allCafes[idx].has_wifi,
            "has_sockets": allCafes[idx].has_sockets,
            "can_take_calls": allCafes[idx].can_take_calls,
            "coffee_price": allCafes[idx].coffee_price

        }
    # print(result)
    # return result
    return jsonify(result=result)


# make api with one random value
@app.route("/random", methods=["GET"])
def randomRoute():
    randomId = random.randint(1, 21)
    newCafe = db.get_or_404(Cafe, randomId)

    # data = {"cafe": {
    #     "name": newCafe.name, "random_mapUrl": newCafe.map_url, "img_url": newCafe.img_url,
    #     "cafe_location" : newCafe.location, "has_sockets" : newCafe.has_sockets, "has_toilet" : newCafe.has_toilet,
    #     "can_take_calls" : newCafe.can_take_calls, "cafe_seats" : newCafe.seats, "coffee_price" : newCafe.coffee_price}}

    newData = jsonify(cafe={
        "name": newCafe.name, "random_mapUrl": newCafe.map_url, "img_url": newCafe.img_url,
        "cafe_location": newCafe.location, "has_sockets": newCafe.has_sockets, "has_toilet": newCafe.has_toilet,
        "can_take_calls": newCafe.can_take_calls, "cafe_seats": newCafe.seats, "coffee_price": newCafe.coffee_price})
    return newData


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
