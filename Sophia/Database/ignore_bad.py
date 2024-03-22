
from Sophia import DATABASE
import asyncio
import random

db = DATABASE["IGNORE_BAD"]

class IGNORE_BAD:
    async def ENABLE(self):
        try:
            await db.update_one({"_id": 1}, {"$addToSet": {"IGNORE_BAD": True}})
            return SUCCESS  # Assuming SUCCESS is defined elsewhere
        except Exception as e:
            print("Error while enabling IGNORE_BAD:", e)
            return f"{e}"  # More informative error

    async def GET(self):
        Find = await db.find_one({"_id": 1})
        return False if Find is None else Find.get("IGNORE_BAD", False)

    async def DISABLE(self):
        try:
            await db.update_one({"_id": 1}, {"$set": {"IGNORE_BAD": False}})
            return SUCCESS
        except Exception as e:
            print(e)
            return f"{e}"
