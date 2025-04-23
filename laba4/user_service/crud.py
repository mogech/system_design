from sqlalchemy.orm import Session
from models import UserDB
from passlib.context import CryptContext

def get_user_by_username(db: Session, username: str):
    return db.query(UserDB).filter(UserDB.username == username).first()

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
