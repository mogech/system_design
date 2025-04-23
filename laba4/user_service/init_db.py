from database import engine, SessionLocal
from models import Base
import crud

def init():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    if not crud.get_user_by_username(db, "admin"):
        crud.create_user(db, "admin", "secret")
    db.close()

if __name__ == "__main__":
    init()
