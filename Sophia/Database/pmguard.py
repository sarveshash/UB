from Sophia import DATABASE
import asyncio

db = DATABASE["PM_GUARD"]

async def SET_PM_GUARD(maximum_warn_count):
    doc = {"_id": 1, "status": True, "warn_count": maximum_warn_count}
    try:
        await db.insert_one(doc)
    except Exception:
        await db.update_one({"_id": 1}, {"$set": {"status": True, "warn_count": maximum_warn_count}})

async def GET_PM_GUARD():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return False
    else:
        value = Find["status"]
        return value

async def GET_WARNING_COUNT():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return None
    else:
        value = Find["warn_count"]
        return value
    
async def UNSET_PM_GUARD():
    await db.update_one({"_id": 1}, {"$set": {"status": False, "warn_count": None}})

async def WARNING_COUNT_GET(user_id):
    Find = await db.find_one({"_id": 1})
    if not Find:
        return None
    else:
        value = Find[user_id]
        return value
async def WARNING_COUNT_REMOVE(user_id):
    await db.update_one({"_id": 1}, {"$set": {f"{user_id}": 0}})
async def WARNING_COUNT_ADD(user_id, count):
    doc = {"_id": 1, f"{user_id}": count}
    await db.insert_one(doc)
