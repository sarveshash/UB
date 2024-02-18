from Sophia import DATABASE
import asyncio

db = DATABASE["afk"]

async def SET_AFK(time, reason):
    doc = {"_id": 1, "stats": True, "time": time, "reason": reason}
    await db.insert_one(doc)
