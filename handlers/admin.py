from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database.db import get_db
from database.models import User, MessageTemplate, Campaign, TelegramAccount, Group
from config.config import config
import json
import os
import logging
logger = logging.getLogger(__name__)

ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",")]

@Client.on_message(filters.command("start"))
async def admin_start(client: Client, message: Message):
    logger.info(f"/start command received from user {message.from_user.id}")
    if message.from_user.id in ADMIN_IDS:
        # Show admin menu
        ...
    else:
        # Show normal user menu or message
        await message.reply_text("Welcome to the bot! Contact admin for more features.")
    """Admin start command with menu"""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Manage Accounts", callback_data="manage_accounts")],
        [InlineKeyboardButton("Manage Templates", callback_data="manage_templates")],
        [InlineKeyboardButton("Manage Campaigns", callback_data="manage_campaigns")],
        [InlineKeyboardButton("Manage Groups", callback_data="manage_groups")]
    ])
    
    await message.reply_text(
        "Admin Panel - Select an option:",
        reply_markup=keyboard
    )

async def manage_accounts(client: Client, message: Message):
    """Show list of accounts with management options"""
    db = next(get_db())
    accounts = db.query(TelegramAccount).all()
    
    if not accounts:
        await message.reply_text("No accounts found.")
        return
    
    keyboard = []
    for account in accounts:
        keyboard.append([
            InlineKeyboardButton(
                f"{account.phone_number} {'✅' if account.is_active else '❌'}",
                callback_data=f"account_detail_{account.id}"
            )
        ])
    
    keyboard.append([InlineKeyboardButton("Add New Account", callback_data="add_account")])
    
    await message.reply_text(
        "Telegram Accounts:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def add_template(client: Client, message: Message, user_id: int):
    """Add a new message template"""
    # This would typically be a conversation handler
    # For simplicity, we'll just show the structure here
    await message.reply_text(
        "Please send the template text. You can use variables like {group_name}."
    )
    # In a real implementation, you would store the user's state and handle the response

async def list_campaigns(client: Client, message: Message):
    """List all campaigns with management options"""
    db = next(get_db())
    campaigns = db.query(Campaign).all()
    
    if not campaigns:
        await message.reply_text("No campaigns found.")
        return
    
    keyboard = []
    for campaign in campaigns:
        keyboard.append([
            InlineKeyboardButton(
                f"{campaign.name} {'✅' if campaign.is_active else '❌'}",
                callback_data=f"campaign_detail_{campaign.id}"
            )
        ])
    
    keyboard.append([InlineKeyboardButton("Create New Campaign", callback_data="create_campaign")])
    
    await message.reply_text(
        "Campaigns:",
        reply_markup=InlineKeyboardMarkup(keyboard)
  )
