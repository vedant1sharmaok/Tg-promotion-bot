from database.db import get_db
from database.models import Campaign, CampaignStat
import pandas as pd
from datetime import datetime, timedelta

def get_campaign_stats(campaign_id: int, days: int = 7):
    """Get statistics for a campaign"""
    db = next(get_db())
    
    # Get basic campaign info
    campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
    if not campaign:
        return None
    
    # Get stats for the last N days
    start_date = datetime.utcnow() - timedelta(days=days)
    stats = db.query(CampaignStat).filter(
        CampaignStat.campaign_id == campaign_id,
        CampaignStat.timestamp >= start_date
    ).all()
    
    # Convert to DataFrame for easier analysis
    df = pd.DataFrame([{
        'timestamp': stat.timestamp,
        'group_id': stat.group_id,
        'account_id': stat.account_id,
        'status': stat.status,
        'error': stat.error_message
    } for stat in stats])
    
    # Calculate metrics
    if not df.empty:
        success_rate = df[df['status'] == 'success'].shape[0] / df.shape[0]
        error_counts = df[df['status'] == 'failed']['error'].value_counts()
    else:
        success_rate = 0
        error_counts = pd.Series()
    
    return {
        'campaign_name': campaign.name,
        'total_messages': df.shape[0],
        'success_rate': success_rate,
        'common_errors': error_counts.to_dict(),
        'timeline': df.groupby([pd.Grouper(key='timestamp', freq='D'), 'status']).size().unstack().fillna(0).to_dict()
    }

def get_account_stats(account_id: int):
    """Get statistics for an account"""
    db = next(get_db())
    
    stats = db.query(CampaignStat).filter(
        CampaignStat.account_id == account_id
    ).all()
    
    df = pd.DataFrame([{
        'timestamp': stat.timestamp,
        'campaign_id': stat.campaign_id,
        'group_id': stat.group_id,
        'status': stat.status
    } for stat in stats])
    
    if not df.empty:
        success_rate = df[df['status'] == 'success'].shape[0] / df.shape[0]
        recent_activity = df['timestamp'].max()
    else:
        success_rate = 0
        recent_activity = None
    
    return {
        'total_messages': df.shape[0],
        'success_rate': success_rate,
        'recent_activity': recent_activity,
        'campaigns': df['campaign_id'].nunique()
    }
