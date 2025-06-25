from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from config.config import config

engine = create_engine(config.DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Import all models to ensure they're registered with SQLAlchemy
    from .models import (
        User,
        TelegramAccount,
        Group,
        MessageTemplate,
        Campaign,
        CampaignAccount,
        CampaignStat
    )
    Base.metadata.create_all(bind=engine, tables=[
        User.__table__,
        TelegramAccount.__table__,
        Group.__table__,
        MessageTemplate.__table__,
        Campaign.__table__,
        CampaignAccount.__table__,
        CampaignStat.__table__
    ])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
