from Sophia import DATABASE
import asyncio
import random

db = DATABASE["Copy_message"]

async def SAVE_MSG(msg_id: int, msg_chat: int):
    try:
        await db.update_one({"_id": 1}, {"$addToSet": {"COPIED": True, "CHAT": msg_chat, "ID": msg_id}})
        return "SUCCESS"
    except Exception as e:
        return str(e)

async def COPIED():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return False
    else:
        value = Find["COPIED"]
        return value

async def UNSAVE_MSG():
    COPIED = await COPIED()
    if not COPIED == True:
        return "ALREADY_EMPTY"
    try:
        await db.update_one({"_id": 1}, {"$addToSet": {"COPIED": False, "CHAT": 0, "ID": 0}})
        return "SUCCESS"
    except Exception as e:
        return str(e)

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
