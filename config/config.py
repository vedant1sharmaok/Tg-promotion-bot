import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database configuration
    DB_URL = os.getenv("DB_URL", "sqlite:///database.db")
    
    # Telegram API configuration
    API_ID = int(os.getenv("API_ID", 12345))
    API_HASH = os.getenv("API_HASH", "your_api_hash")
    
    # Bot configuration
    ADMIN_IDS = [int(id) for id in os.getenv("ADMIN_IDS", "").split(",") if id]
    MAX_ACCOUNTS_PER_USER = int(os.getenv("MAX_ACCOUNTS_PER_USER", 5))
    
    # Rate limiting
    MESSAGES_PER_MINUTE = int(os.getenv("MESSAGES_PER_MINUTE", 20))
    DELAY_BETWEEN_GROUPS = int(os.getenv("DELAY_BETWEEN_GROUPS", 30))
    
    # Proxy settings
    PROXY_ENABLED = os.getenv("PROXY_ENABLED", "False").lower() == "true"
    PROXY = {
        "scheme": os.getenv("PROXY_SCHEME", "socks5"),
        "hostname": os.getenv("PROXY_HOST", ""),
        "port": int(os.getenv("PROXY_PORT", 1080)),
        "username": os.getenv("PROXY_USER", ""),
        "password": os.getenv("PROXY_PASS", "")
    } if PROXY_ENABLED else None

config = Config()
