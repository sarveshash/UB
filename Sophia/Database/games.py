from Sophia import GAME_DATABASE
import asyncio

db = GAME_DATABASE["Games_500"]

async def GET_AVAILABLE_USERS():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return []
    else:
        value = Find.get("USERS", [])
        return value

async def ADD_NEW_USER(user_id):
    await db.update_one({"_id": 1}, {"$addToSet": {"USERS": user_id}}, upsert=True)

async def REMOVE_USER(user_id):
    await db.update_one({"_id": 1}, {"$pull": {"USERS": user_id}})

async def GET_COINS_FROM_USER(user_id: int):
    USER_ACC = await GET_AVAILABLE_USERS()
    if user_id not in USER_ACC:
        return "USER_NOT_FOUND"
    string = {"user_id": user_id}
    xx = db.find_one(string)
    mm = int(xx["coins"])
    return mm

async def ADD_COINS(user_id: int, coins: int):
    USER_ACC = await GET_AVAILABLE_USERS()
    if user_id not in USER_ACC:
        return "USER_NOT_FOUND"
    COINS_USR = await GET_COINS_FROM_USER(user_id)
    TOTAL_COINS = COINS_USR+coins
    filter = {"user_id": user_id}
    update = {"$set": {"coins": TOTAL_COINS}}
    await db.update_one(filter, update)
  
