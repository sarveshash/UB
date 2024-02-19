from Sophia import GAME_DATABASE
import asyncio

db = GAME_DATABASE["Games"]

async def GET_AVAILABLE_USERS():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return []  # Return an empty list if no approved users are found
    else:
        value = Find.get("USERS", [])  # Ensure default value is an empty list
        return value

async def ADD_NEW_USER(user_id):
    await db.update_one({"_id": 1}, {"$addToSet": {"USERS": user_id}}, upsert=True)

async def REMOVE_USER(user_id):
    await db.update_one({"_id": 1}, {"$pull": {"USERS": user_id}})

async def ADD_COINS_TO_USER(user_id, coins):
    available_users = await GET_AVAILABLE_USERS()
    if user_id not in available_users:
        await ADD_NEW_USER(user_id)
    doc = {"_id": 5, f"{user_id}": coins}
    try:
        await db.insert_one(doc)
    except Exception:
        await db.update_one({"_id": 1}, {"$set": {f"{user_id}": coins}})
        
async def GET_USER_COINS(user_id):
    Find = await db.find_one({"_id": 5})
    if not Find:
        return None
    else:
        value = Find[f"{user_id}"]
        return value

async def SEND_COINS(from_user, to_user, coins):
    USER_COINS = await GET_USER_COINS(from_user)
    if USER_COINS >= coins:
        try:
            coins_str = f"-{coins}"
            coins_int = int(coins_str)
            await ADD_COINS_TO_USER(from_user, coins_str)
            await ADD_COINS_TO_USER(to_user, coins)
            return True
        except Exception as e:
            return e
    else:
        return "LOW_COINS"
