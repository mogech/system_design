from database import posts_collection
from datetime import datetime, timezone

def init():
    if posts_collection.count_documents({}) == 0:
        posts_collection.insert_many([
            {
                "content": "Hello, Mongo!",
                "author": "admin",
                "created_at": datetime.now(timezone.utc)
            },
            {
                "content": "Test",
                "author": "test_user",
                "created_at": datetime.now(timezone.utc)
            }
        ])
        print("Test posts inserted.")

if __name__ == "__main__":
    init()