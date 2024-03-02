from Sophia import DATABASE
import asyncio
import random

db = DATABASE["Copy_message"]

async def SAVE_MSG(msg_id: int, msg_chat: int):
    await db.update_one({"_id": 1}, {"$addToSet": {"COPIED": True, "CHAT": msg_chat, "ID": msg_id}})

async def COPIED():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return False
    else:
        value = Find["COPIED"]
        return value

async def CHAT_ID():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return False
    else:
        value = Find["CHAT"]
        return value

async def MSG_ID():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return False
    else:
        value = Find["ID"]
        return value
