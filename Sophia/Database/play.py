from Sophia import DATABASE
import asyncio
import random
import logging

db = DATABASE["playgroups"]

class play:
    async def get():
        try:
            info = await db.find_one({"_id": 1})
            return info
        except Exception as e:
            logging.error(e)
            return str(e)
    async def addRemove(chat_id, addOrRemove='add'):
        try:
            if addOrRemove == 'add':
                await db.update_one({"_id": 1}, {"$addToSet": {"chats": chat_id}})
            elif addOrRemove == 'remove':
                await db.update_one({"_id": 1}, {"$pull": {"chats": chat_id}})
            else:
                return "Invalid operation"
            return "SUCCESS"
        except Exception as e:
            logging.error(e)
            return str(e)
