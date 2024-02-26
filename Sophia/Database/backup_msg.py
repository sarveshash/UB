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

async def ADD_BACKUP_CHAT(chat_id: int):
    await db.update_one({"_id": 1}, {"$addToSet": {"CHATS": chat_id}}, upsert=True)

async def REMOVE_BACKUP_CHAT(chat_id: int):
    await db.update_one({"_id": 1}, {"$pull": {"CHATS": chat_id}})

async def SET_BACKUP_CHANNEL_ID(user_id, channel_id):
    await await db.update_one({"_id": 1}, {"$addToSet": {f"{user_id}": channel_id}})

async def GET_BACKUP_CHANNEL_ID(chat_id):
    Find = await db.find_one({"_id": 1})
    if not Find:
        return False
    else:
        channel = Find[f"{chat_id}"]
        return channel
        
