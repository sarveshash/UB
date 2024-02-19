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

async def GET_APPROVED_USERS():
    Find = await db.find_one({"_id": 2})
    if not Find:
        return None
    else:
        value = Find["approved_users"]
        return value

async def ADD_APPROVED_USER(user_id):
    doc = {"_id": 2, "approved_users": [0]}
    try:
        await db.insert_one(doc)
        await db.update_one({"_id": 2}, {"$push": {"approved_users": user_id}})
    except Exception:
        await db.update_one({"_id": 2}, {"$push": {"approved_users": user_id}})
