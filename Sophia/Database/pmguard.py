from Sophia import DATABASE
import asyncio

db = DATABASE["PM_GUARD"]

async def SET_PM_GUARD():
    doc = {"_id": 1, "status": True}
    await db.insert_one(doc)

async def UNSET_PM_GUARD():
    await db.update_one({"_id": 1}, {"$set": {"status": False}})

async def WARNING_COUNT_GET(user_id):
    Find = await db.find_one({"_id": 1})
    if not Find:
        return None
    else:
        value = Find[user_id]
        return value
async def WARNING_COUNT_REMOVE(user_id):
    await db.update_one({"_id": 1}, {"$set": {"user_id": 0}})
async def WARNING_COUNT_ADD(user_id, count):
    doc = {"_id": 1, f"{user_id}": count}
    await db.insert_one(doc)
