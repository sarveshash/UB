from Sophia import DATABASE
import asyncio
import random

db = GAME_DATABASE["Games_RO"]

async def SAVE_MSG(msg_id: int, msg_chat: int):
    await db.update_one({"_id": 1}, {"$addToSet": {"STATUS": True}, {"CHAT": msg_chat}, {"ID": msg_id}}
