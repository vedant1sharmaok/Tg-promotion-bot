from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from config.config import config

engine = create_engine(config.DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
