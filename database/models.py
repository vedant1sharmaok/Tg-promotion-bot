from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    accounts = relationship("TelegramAccount", back_populates="user")
    campaigns = relationship("Campaign", back_populates="user")

class TelegramAccount(Base):
    __tablename__ = 'telegram_accounts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    session_string = Column(String, nullable=False)
    phone_number = Column(String)
    is_active = Column(Boolean, default=True)
    last_used = Column(DateTime)
    
    user = relationship("User", back_populates="accounts")
    campaigns = relationship("CampaignAccount", back_populates="account")

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, unique=True)
    title = Column(String)
    username = Column(String)
    members_count = Column(Integer)
    is_active = Column(Boolean, default=True)
    added_at = Column(DateTime, default=datetime.utcnow)

class MessageTemplate(Base):
    __tablename__ = 'message_templates'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    text = Column(Text)
    photo_path = Column(String)
    variables = Column(String)  # JSON string of available variables
    
    campaigns = relationship("Campaign", back_populates="template")

class Campaign(Base):
    __tablename__ = 'campaigns'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    template_id = Column(Integer, ForeignKey('message_templates.id'))
    name = Column(String)
    is_active = Column(Boolean, default=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    interval_minutes = Column(Integer)  # Interval between sending rounds
    delay_seconds = Column(Integer)  # Delay between groups
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="campaigns")
    template = relationship("MessageTemplate", back_populates="campaigns")
    accounts = relationship("CampaignAccount", back_populates="campaign")
    stats = relationship("CampaignStat", back_populates="campaign")

class CampaignAccount(Base):
    __tablename__ = 'campaign_accounts'
    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey('campaigns.id'))
    account_id = Column(Integer, ForeignKey('telegram_accounts.id'))
    
    campaign = relationship("Campaign", back_populates="accounts")
    account = relationship("TelegramAccount", back_populates="campaigns")

class CampaignStat(Base):
    __tablename__ = 'campaign_stats'
    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey('campaigns.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)
    group_id = Column(Integer)
    account_id = Column(Integer)
    status = Column(String)  # 'success', 'failed', 'skipped'
    error_message = Column(String)
    
    campaign = relationship("Campaign", back_populates="stats")
