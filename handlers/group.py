from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database.db import get_db
from database.models import Group
from config.config import config
from utilities.scraper import scrape_public_groups
import asyncio

@Client.on_message(filters.command("groups") & filters.user(config.ADMIN_IDS))
async def manage_groups(client: Client, message: Message):
    """Show group management interface"""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("List Groups", callback_data="list_groups")],
        [InlineKeyboardButton("Scrape New Groups", callback_data="scrape_groups")],
        [InlineKeyboardButton("Update Members Count", callback_data="update_members")],
        [InlineKeyboardButton("Export Groups", callback_data="export_groups")]
    ])
    
    await message.reply_text(
        "Group Management - Select an option:",
        reply_markup=keyboard
    )

async def list_all_groups(client: Client, message: Message, page: int = 0, per_page: int = 10):
    """List groups with pagination"""
    db = next(get_db())
    groups = db.query(Group).order_by(Group.title).offset(page*per_page).limit(per_page).all()
    total = db.query(Group).count()
    
    if not groups:
        await message.reply_text("No groups found in database.")
        return
    
    response = f"**Groups ({page*per_page+1}-{min((page+1)*per_page, total)} of {total})**\n\n"
    for group in groups:
        response += f"• {group.title} ({group.group_id})"
        if group.username:
            response += f" @{group.username}"
        response += f" - {group.members_count or '?'} members\n"
        response += "✅ Active\n" if group.is_active else "❌ Inactive\n"
    
    keyboard = []
    if page > 0:
        keyboard.append(InlineKeyboardButton("⬅️ Previous", callback_data=f"groups_page_{page-1}"))
    if (page+1)*per_page < total:
        keyboard.append(InlineKeyboardButton("Next ➡️", callback_data=f"groups_page_{page+1}"))
    
    await message.reply_text(
        response,
        reply_markup=InlineKeyboardMarkup([keyboard]) if keyboard else None
    )

async def scrape_groups_interactive(client: Client, message: Message):
    """Start interactive group scraping"""
    await message.reply_text(
        "Please send me keywords to search for groups, separated by commas.\n\n"
        "Example: `technology, programming, crypto`"
    )
    # In a complete implementation, you would store the user's state and handle the response

async def toggle_group_active(client: Client, group_id: int):
    """Toggle group active status"""
    db = next(get_db())
    group = db.query(Group).filter(Group.group_id == group_id).first()
    if group:
        group.is_active = not group.is_active
        db.commit()
        return True, f"Group {group.title} is now {'active' if group.is_active else 'inactive'}"
    return False, "Group not found"

async def export_groups(client: Client, message: Message):
    """Export groups to a file"""
    db = next(get_db())
    groups = db.query(Group).all()
    
    if not groups:
        await message.reply_text("No groups to export.")
        return
    
    # Create CSV content
    csv_content = "id,title,username,members_count,is_active\n"
    for group in groups:
        csv_content += (
            f"{group.group_id},"
            f'"{group.title}",'
            f"{group.username or ''},"
            f"{group.members_count or 0},"
            f"{int(group.is_active)}\n"
        )
    
    # Send as document
    await client.send_document(
        chat_id=message.chat.id,
        document="groups_export.csv",
        file_name="groups_export.csv",
        caption="Here's your groups export"
  )
