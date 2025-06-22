from pyrogram import Client, idle
from config.config import config
from database.db import init_db
from handlers.auth import login_with_session_string, login_with_otp
from handlers.message import schedule_existing_campaigns
from handlers.admin import admin_start, manage_accounts, add_template, list_campaigns
from utilities.scraper import scrape_public_groups, update_group_members_count
import asyncio
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize database
init_db()

# Create Pyrogram client
app = Client(
    "promotion_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=os.getenv("BOT_TOKEN"),
    proxy=config.PROXY
)

# Register handlers
app.on_message(filters.command("start") & filters.user(config.ADMIN_IDS))(admin_start)
app.on_message(filters.command("accounts") & filters.user(config.ADMIN_IDS))(manage_accounts)
app.on_message(filters.command("templates") & filters.user(config.ADMIN_IDS))(add_template)
app.on_message(filters.command("campaigns") & filters.user(config.ADMIN_IDS))(list_campaigns)

async def main():
    await app.start()
    logger.info("Bot started")
    
    # Schedule existing campaigns
    schedule_existing_campaigns()
    
    # Example: Scrape groups for "technology" keyword
    # await scrape_public_groups(app, ["technology"])
    
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
