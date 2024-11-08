from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startupDBClient():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("connected to MongoDB database!!! ")

@app.on_event("shutdown")
def shutDown_db_client():
    app.mongodb_client.close()


