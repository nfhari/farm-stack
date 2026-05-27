from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
app = FastAPI()
mongo_url = os.getenv("MONGO_URL")
client = MongoClient(mongo_url)
# Connect to MongoDB container
#client = MongoClient("mongodb://mongodb:27017")

# Create database
db = client["farm_db"]

# Create collection
users = db["users"]

@app.get("/")
def home():
    return {"message": "MongoDB connected successfully"}

@app.get("/add")
def add_user():

    user = {
        "name": "Prasad",
        "role": "QA Engineer"
    }

    users.insert_one(user)

    return {"message": "User inserted"}