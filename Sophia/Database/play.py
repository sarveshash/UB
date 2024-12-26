from Sophia import DATABASE
import asyncio
import random
import logging

db = DATABASE["playgroups"]

class play:
    async def get(self):
        try:
            info = await db.find_one({"_id": 1})
            return info or ''
        except Exception as e:
            logging.error(e)
            return str(e)
    async def addRemove(self, chat_id, addOrRemove='add'):
        try:
            if addOrRemove == 'add':
                info = await db.find_one({"_id": 1})
                if chat_id in info:
                    return 'ALREADY'
                await db.update_one({"_id": 1}, {"$addToSet": {"chats": chat_id}})
            elif addOrRemove == 'remove':
                if chat_id in info:
                    await db.update_one({"_id": 1}, {"$pull": {"chats": chat_id}})
                else: return 'ALREADY'
            else:
                return "Invalid operation"
            return "SUCCESS"
        except Exception as e:
            logging.error(e)
            return str(e)
