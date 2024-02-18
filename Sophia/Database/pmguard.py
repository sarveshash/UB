from Sophia import DATABASE
import asyncio

db = DATABASE["PM_GUARD"]

async def SET_PM_GUARD():
    doc = {"_id": 1, "status": True}
    await db.insert_one(doc)

async def UNSET_PM_GUARD():
    await db.update_one({"_id": 1}, {"$set": {"status": False}})

async def WARNING_COUNT_GET(user_id):
  
async def WARNING_COUNT_REMOVE(user_id):

async def WARNING_COUNT_ADD(user_id):
  
