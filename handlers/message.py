from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database.db import get_db
from database.models import MessageTemplate, Campaign, TelegramAccount, Group
from config.config import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import json

scheduler = AsyncIOScheduler()

async def send_promotion_message(client: Client, group_id: int, template: MessageTemplate, account_id: int, campaign_id: int):
    """Send promotion message to a specific group"""
    db = next(get_db())
    
    try:
        # Format message with variables
        message_text = template.text
        # Here you could add variable replacement logic
        
        if template.photo_path:
            await client.send_photo(
                chat_id=group_id,
                photo=template.photo_path,
                caption=message_text
            )
        else:
            await client.send_message(
                chat_id=group_id,
                text=message_text
            )
        
        # Log successful delivery
        stat = CampaignStat(
            campaign_id=campaign_id,
            group_id=group_id,
            account_id=account_id,
            status="success"
        )
        db.add(stat)
        db.commit()
        return True
    except Exception as e:
        # Log failure
        stat = CampaignStat(
            campaign_id=campaign_id,
            group_id=group_id,
            account_id=account_id,
            status="failed",
            error_message=str(e)
        )
        db.add(stat)
        db.commit()
        return False

async def run_campaign(campaign_id: int):
    """Run a campaign by sending messages to all groups with selected accounts"""
    db = next(get_db())
    campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
    if not campaign or not campaign.is_active:
        return
    
    # Get all accounts assigned to this campaign
    accounts = [ca.account for ca in campaign.accounts if ca.account.is_active]
    if not accounts:
        return
    
    # Get all active groups
    groups = db.query(Group).filter(Group.is_active == True).all()
    if not groups:
        return
    
    # Create clients for all accounts
    clients = []
    for account in accounts:
        try:
            client = Client(
                name=f"account_{account.id}",
                session_string=account.session_string,
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                proxy=config.PROXY
            )
            await client.start()
            clients.append((client, account.id))
        except Exception as e:
            print(f"Failed to start client for account {account.id}: {str(e)}")
    
    # Send messages with rate limiting
    for group in groups:
        for client, account_id in clients:
            success = await send_promotion_message(
                client=client,
                group_id=group.group_id,
                template=campaign.template,
                account_id=account_id,
                campaign_id=campaign.id
            )
            
            if not success:
                # Skip to next account if failed
                continue
            
            # Respect delay between groups
            await asyncio.sleep(campaign.delay_seconds)
        
        # Respect global rate limits
        await asyncio.sleep(config.MESSAGES_PER_MINUTE / 60)
    
    # Stop all clients
    for client, _ in clients:
        await client.stop()
    
    # Schedule next run if campaign is recurring
    if campaign.interval_minutes > 0:
        scheduler.add_job(
            run_campaign,
            'interval',
            minutes=campaign.interval_minutes,
            args=[campaign.id],
            id=f"campaign_{campaign.id}"
        )

def schedule_existing_campaigns():
    """Schedule all active campaigns on startup"""
    db = next(get_db())
    campaigns = db.query(Campaign).filter(Campaign.is_active == True).all()
    
    for campaign in campaigns:
        scheduler.add_job(
            run_campaign,
            'interval',
            minutes=campaign.interval_minutes,
            args=[campaign.id],
            id=f"campaign_{campaign.id}"
        )
    
    scheduler.start()
