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
    try:
        await db.insert_one({"_id": 5, f"{user_id}": coins}, upsert=True)
    except Exception:
        await db.update_one({"_id": 1}, {"$set": {f"{user_id}": coins}}, upsert=True)
        
async def GET_USER_COINS(user_id):
    Find = await db.find_one({"_id": 5})
    if not Find or f"{user_id}" not in Find:
        return None
    else:
        value = Find[f"{user_id}"]
        return value
        
async def SEND_COINS(from_user, to_user, coins):
    from_user_coins = await GET_USER_COINS(f"{from_user}")
    if from_user_coins is None:
        return "SENDER_NOT_FOUND"
    if from_user_coins < coins:
        return "LOW_COINS"
    to_user_coins = await GET_USER_COINS(f"{to_user}")
    if to_user_coins is None:
        return "RECIPIENT_NOT_FOUND"
    try:
        await ADD_COINS_TO_USER(from_user, from_user_coins - coins)
        await ADD_COINS_TO_USER(to_user, to_user_coins + coins)
        return True
    except Exception as e:
        print(f"Error sending coins from {from_user} to {to_user}: {e}")
        return "SEND_COINS_FAILED"
