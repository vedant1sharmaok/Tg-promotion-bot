from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
from database.db import get_db
from config.config import config
import asyncio

class Scheduler:
    def __init__(self):
        self.scheduler = AsyncIOScheduler(
            jobstores={
                'default': SQLAlchemyJobStore(
                    engine=get_db().bind,
                    tablename='scheduled_jobs'
                )
            },
            executors={
                'default': ThreadPoolExecutor(20)
            },
            job_defaults={
                'coalesce': True,
                'max_instances': 3,
                'misfire_grace_time': 60*15
            }
        )
    
    async def start(self):
        """Start the scheduler"""
        self.scheduler.start()
    
    async def shutdown(self):
        """Shutdown the scheduler gracefully"""
        self.scheduler.shutdown(wait=True)
    
    async def schedule_campaign(self, campaign_id: int, interval_minutes: int):
        """Schedule a campaign to run at regular intervals"""
        self.scheduler.add_job(
            self._run_campaign,
            'interval',
            minutes=interval_minutes,
            args=[campaign_id],
            id=f'campaign_{campaign_id}',
            replace_existing=True
        )
    
    async def schedule_immediate_run(self, campaign_id: int):
        """Schedule a campaign to run immediately once"""
        self.scheduler.add_job(
            self._run_campaign,
            'date',
            args=[campaign_id],
            id=f'campaign_once_{campaign_id}'
        )
    
    async def _run_campaign(self, campaign_id: int):
        """Internal method to run campaign"""
        from handlers.message import run_campaign
        await run_campaign(campaign_id)
    
    async def reschedule_all_campaigns(self):
        """Reschedule all active campaigns from database"""
        from database.models import Campaign
        db = next(get_db())
        campaigns = db.query(Campaign).filter(Campaign.is_active == True).all()
        
        for campaign in campaigns:
            await self.schedule_campaign(
                campaign.id,
                campaign.interval_minutes
            )

# Global scheduler instance
scheduler = Scheduler()
