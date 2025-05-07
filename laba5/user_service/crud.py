from sqlalchemy.orm import Session
from models import UserDB
from passlib.context import CryptContext
from cache import get_user_from_cache, set_user_to_cache

def get_user_by_username(db: Session, username: str):
    cached_user = get_user_from_cache(username)
    if cached_user:
        return UserDB(**cached_user)

    user = db.query(UserDB).filter(UserDB.username == username).first()
    if user:
        set_user_to_cache(username, {"id": user.id, "username": user.username, "password": user.password})
    return user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, username: str, password: str):
    hashed_password = pwd_context.hash(password)
    db_user = UserDB(username=username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db: Session):
    return db.query(UserDB).all()
