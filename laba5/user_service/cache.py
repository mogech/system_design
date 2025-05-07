import redis
import json

redis_client = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)

def get_user_from_cache(username: str):
    data = redis_client.get(username)
    if data:
        return json.loads(data)
    return None

def set_user_to_cache(username: str, user_data: dict):
    redis_client.set(username, json.dumps(user_data), ex=300)
