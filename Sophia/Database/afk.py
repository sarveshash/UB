from Sophia import DATABASE
import asyncio

db = DATABASE["afk"]

async def SET_AFK(time, reason):
    doc = {"_id": 1, "stats": True, "time": time, "reason": reason}
    await db.insert_one(doc)

async def UNSET_AFK():
    await db.update_one({"_id": 1}, {"$set": {"stats": False, "time": None, "reason": None}})
    
async def GET_AFK():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return False
    else:
        stats = Find["stats"]
        return stats
