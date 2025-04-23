from database import posts_collection
from models import WallPost
from bson import ObjectId

def create_post(post: WallPost):
    post_dict = post.model_dump()
    post_dict["created_at"] = post.created_at
    result = posts_collection.insert_one(post_dict)
    post.id = str(result.inserted_id)
    return post

def get_posts():
    posts = []
    for doc in posts_collection.find():
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        posts.append(WallPost(**doc))
    return posts

def get_post_by_id(post_id: str):
    doc = posts_collection.find_one({"_id": ObjectId(post_id)})
    if not doc:
        return None
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return WallPost(**doc)

def delete_post(post_id: str):
    return posts_collection.delete_one({"_id": ObjectId(post_id)}).deleted_count > 0