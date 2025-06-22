from pyrogram import Client
from database.db import get_db
from database.models import Group
from config.config import config
import asyncio

async def scrape_public_groups(client: Client, keywords: list, limit: int = 20):
    """Search for public groups by keywords and add them to database"""
    db = next(get_db())
    
    for keyword in keywords:
        async for dialog in client.search_global(keyword, limit=limit):
            if dialog.chat and dialog.chat.type in ["group", "supergroup"]:
                # Check if group already exists
                existing = db.query(Group).filter(Group.group_id == dialog.chat.id).first()
                if existing:
                    continue
                
                # Add new group
                group = Group(
                    group_id=dialog.chat.id,
                    title=dialog.chat.title,
                    username=getattr(dialog.chat, "username", None),
                    members_count=getattr(dialog.chat, "members_count", 0),
                    is_active=True
                )
                db.add(group)
        
        db.commit()
        await asyncio.sleep(5)  # Respect rate limits

async def update_group_members_count(client: Client):
    """Update members count for all groups in database"""
    db = next(get_db())
    groups = db.query(Group).filter(Group.is_active == True).all()
    
    for group in groups:
        try:
            chat = await client.get_chat(group.group_id)
            group.members_count = getattr(chat, "members_count", 0)
            db.commit()
        except Exception as e:
            print(f"Failed to update group {group.group_id}: {str(e)}")
            group.is_active = False
            db.commit()
        
        await asyncio.sleep(2)  # Respect rate limits
