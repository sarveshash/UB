from Sophia import DATABASE
import asyncio

db = DATABASE["Sophia"]["afk"]

async def SET_AFK(stats, reason_available, time, reason):
    
