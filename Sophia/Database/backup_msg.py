from Sophia import DATABASE
import asyncio

db = DATABASE["BACKUP_MESSAGE"]

async def ENABLE_BACKUP():
    doc = {"_id": 1, "stats": True}
    try:
        await db.insert_one(doc)
    except Exception:
        await db.update_one({"_id": 1}, {"$set": {"stats": True}})
        
async def DISABLE_BACKUP():
    await db.update_one({"_id": 1}, {"$set": {"stats": False}})

async def GET_BACKUP():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return False
    else:
        stats = Find["stats"]
        return stats
