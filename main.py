from pyrogram import Client, idle, filters
from config.config import config
from database.db import init_db
from handlers.auth import login_with_session_string, login_with_otp
from handlers.message import schedule_existing_campaigns
from handlers.admin import admin_start, manage_accounts, add_template, list_campaigns
from utilities.scraper import scrape_public_groups, update_group_members_count
import asyncio
import os
import logging
from flask import Flask
import threading

def start_health_server():
    app = Flask(__name__)

    @app.route("/")
    def health():
        return "OK", 200

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=start_health_server, daemon=True).start()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

init_db()

# Bot token check
bot_token = os.getenv("BOT_TOKEN")
if not bot_token:
    raise ValueError("BOT_TOKEN environment variable not set")

# Create Pyrogram bot client
app = Client(
    "promotion_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=bot_token,
    proxy=config.PROXY
)

app.on_message(filters.command("start"))(admin_start)
app.on_message(filters.command("accounts"))(manage_accounts)
app.on_message(filters.command("templates"))(add_template)
app.on_message(filters.command("campaigns"))(list_campaigns)

async def main():
    await app.start()
    logger.info("Bot started")
    
    schedule_existing_campaigns()
    
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
    
