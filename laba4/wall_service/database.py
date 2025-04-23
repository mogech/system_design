from pymongo import MongoClient, ASCENDING
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = MongoClient(MONGO_URL)
db = client["wall_db"]
posts_collection = db["posts"]

posts_collection.create_index([("author", ASCENDING)])