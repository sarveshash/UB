from Sophia import GAME_DATABASE
import asyncio

db = GAME_DATABASE["Games"]

async def ADD_COINS(user_id, coins):
    doc = {"_id": 1, f"{user_id}": coins}
    try:
        await db.insert_one(doc)
    except Exception:
        await db.update_one({"_id": 1}, {"$set": {f"{user_id}": coins}})
        
async def GET_USER_COINS(user_id):
    Find = await db.find_one({"_id": 1})
    if not Find:
        return None
    else:
        value = Find[f"{user_id}"]
        return value
