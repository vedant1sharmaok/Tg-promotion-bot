from pyrogram import Client, filters
from pyrogram.types import Message
from database.db import get_db
from database.models import User, TelegramAccount
from config.config import config
import os

async def login_with_session_string(session_string: str, phone_number: str = None, user_id: int = None):
    """Login to Telegram account using session string"""
    try:
        client = Client(
            name=f"account_{phone_number or user_id}",
            session_string=session_string,
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            proxy=config.PROXY
        )
        
        await client.start()
        me = await client.get_me()
        
        # Store account in database
        db = next(get_db())
        user = db.query(User).filter(User.telegram_id == user_id).first()
        if not user:
            user = User(telegram_id=user_id)
            db.add(user)
            db.commit()
        
        account = TelegramAccount(
            user_id=user.id,
            session_string=session_string,
            phone_number=phone_number or me.phone_number,
            is_active=True
        )
        db.add(account)
        db.commit()
        
        await client.stop()
        return True, "Login successful"
    except Exception as e:
        return False, f"Login failed: {str(e)}"

async def login_with_otp(phone_number: str, otp: str, password: str = None, user_id: int = None):
    """Login to Telegram account using OTP and optional password"""
    try:
        client = Client(
            name=f"account_{phone_number}",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            proxy=config.PROXY
        )
        
        await client.connect()
        
        # Send OTP request
        sent_code = await client.send_code(phone_number)
        
        # Sign in with OTP
        await client.sign_in(
            phone_number,
            sent_code.phone_code_hash,
            otp
        )
        
        # If 2FA password is required
        if password:
            await client.check_password(password)
        
        # Get session string
        session_string = await client.export_session_string()
        
        # Store account in database
        db = next(get_db())
        user = db.query(User).filter(User.telegram_id == user_id).first()
        if not user:
            user = User(telegram_id=user_id)
            db.add(user)
            db.commit()
        
        account = TelegramAccount(
            user_id=user.id,
            session_string=session_string,
            phone_number=phone_number,
            is_active=True
        )
        db.add(account)
        db.commit()
        
        await client.disconnect()
        return True, "Login successful"
    except Exception as e:
        return False, f"Login failed: {str(e)}"
