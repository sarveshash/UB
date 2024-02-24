from Sophia import DATABASE
import asyncio


db = DATABASE["BROADCAST"]

async def ADD_ANY_CHAT_ID(id: int):
    await db.update_one({"_id": 3}, {"$addToSet": {"CHATS": id}}, upsert=True)

async def ADD_GROUP_ID(id: int):
    await db.update_one({"_id": 4}, {"$addToSet": {"GROUPS": id}}, upsert=True)

async def ADD_USER_ID(id: int):
    await db.update_one({"_id": 5}, {"$addToSet": {"USERS": id}}, upsert=True)

async def GET_ALL_CHATS():
    Find = await db.find_one({"_id": 3})
    if not Find:
        return []
    else:
        value = Find.get("CHATS", [])
        return value

async def GET_ALL_GROUPS():
    Find = await db.find_one({"_id": 4})
    if not Find:
        return []
    else:
        value = Find.get("GROUPS", [])
        return value

async def GET_ALL_USERS():
    Find = await db.find_one({"_id": 5})
    if not Find:
        return []
    else:
        value = Find.get("USERS", [])
        return value
