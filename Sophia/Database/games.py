from Sophia import GAME_DATABASE
import asyncio
import random

db = GAME_DATABASE["Games_R"]

async def GET_AVAILABLE_USERS():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return []
    else:
        value = Find.get("USERS", [])
        return value

async def ADD_NEW_USER(user_id):
    doc = {"_id": 4444 + user_id, "NAME": "Steve_HS"}
    await db.insert_one(doc)
    await db.update_one({"_id": 1}, {"$addToSet": {"USERS": user_id}}, upsert=True)

async def GET_COINS_FROM_USER(user_id: int):
    document_id = f"user_{user_id}"
    try:
        user_data = await db.find_one({"_id": document_id})
        if user_data:
            return user_data.get("coins", 0)
        else:
            return 0  # Handle case where user document is not found
    except Exception as e:
        # Handle exceptions
        print(f"Error getting coins for user {user_id}: {e}")
        return 0

async def ADD_COINS(user_id: int, coins: int):
    document_id = f"user_{user_id}"
    try:
        await db.update_one(
            {"_id": document_id},
            {"$inc": {"coins": coins}},
            upsert=True
        )
    except Exception as e:
        # Handle exceptions
        print(f"Error updating coins for user {user_id}: {e}")

async def REMOVE_USER(user_id):
    document_id = f"user_{user_id}"
    await db.delete_one({"_id": document_id})
    await db.update_one({"_id": 1}, {"$pull": {"USERS": user_id}})
    try:
        await db.delete_one({"_id": 888 + user_id})
    except Exception as e:
        print("Its normal error i guess", e)
    try:
        await db.delete_one({"_id": 4444 + user_id})
    except Exception as e:
        print("Its normal error i guess", e)
    
    
async def SEND_COINS(from_user: int, to_user: int, coins: int):
    USERS_ACC = await GET_AVAILABLE_USERS()
    if from_user not in USERS_ACC:
        return "FROM_USER_NOT_FOUND"
    elif to_user not in USERS_ACC:
        return "TO_USER_NOT_FOUND"
    COINS_FR_USR = await GET_COINS_FROM_USER(from_user)
    if coins > COINS_FR_USR:
        return "NOT_ENOUGH_COINS"
    elif coins <= 0:
        return "NOT_POSTIVE_NUMBER"
    elif coins <= COINS_FR_USR:
        try:
            await ADD_COINS(from_user, -coins)
            await ADD_COINS(to_user, coins)
            return "SUCCESS"
        except Exception as e:
            ERROR_RETURN_STR = f"ERROR, {e}"
            return ERROR_RETURN_STR

async def SET_PROFILE_PIC(user_id: int, image: str):
    USERS_ACC = await GET_AVAILABLE_USERS()
    if user_id not in USERS_ACC:
        return "USER_NOT_FOUND"
    COINS_USR = await GET_COINS_FROM_USER(user_id)
    if COINS_USR >= 1000:
        await ADD_COINS(user_id, -1000)
        doc = {"_id": 888 + user_id, "IMAGE": image}
        try:
            await db.insert_one(doc)
        except Exception:
            await db.update_one({"_id": 888 + user_id}, {"$set": {"IMAGE": image}})
        return "SUCCESS"
    else:
        return "NOT_ENOUGH_COINS"

async def GET_PROFILE_PIC(user_id):
    Find = await db.find_one({"_id": 888 + user_id})
    if not Find:
        return None
    else:
        value = Find["IMAGE"]
        return value

async def SET_USER_NAME(user_id: int, name: str):
    USERS_ACC = await GET_AVAILABLE_USERS()
    if user_id not in USERS_ACC:
        return "USER_NOT_FOUND"
    COINS_USR = await GET_COINS_FROM_USER(user_id)
    if COINS_USR >= 1999:
        await ADD_COINS(user_id, -1999)
        doc = {"_id": 4444 + user_id, "NAME": name}
        try:
            await db.insert_one(doc)
        except Exception:
            await db.update_one({"_id": 4444 + user_id}, {"$set": {"NAME": name}})
        return "SUCCESS"
    else:
        return "NOT_ENOUGH_COINS"


async def GET_USER_NAME(user_id):
    Find = await db.find_one({"_id": 4444 + user_id})
    if not Find:
        return None
    else:
        value = Find["NAME"]
        return value
        

async def BET_COINS(user_id: int, coins: int):
    USERS_ACC = await GET_AVAILABLE_USERS()
    if user_id not in USERS_ACC:
        return "USER_NOT_FOUND"
    COINS_USR = await GET_COINS_FROM_USER(user_id)
    if coins > COINS_USR:
        return "NOT_ENOUGH_COINS"
    elif coins <= 0:
        return "NOT_POSTIVE_NUMBER"
    elif coins <= COINS_USR:
        try:
            LUCK_LIST = ['YES', 'NO']
            PER_50 = (coins / 100) * 50
            PER_50 = int(PER_50)
            RANDOM_COINS = random.randint(PER_50, coins)
            RANDOM_COINS = RANDOM_COINS+10
            GET_LUCK = random.choice(LUCK_LIST)
            if GET_LUCK == 'YES':
                await ADD_COINS(user_id, RANDOM_COINS)
                RANDOM_COINS = str(RANDOM_COINS)
                return RANDOM_COINS
            elif GET_LUCK == 'NO':
                mins_coins = f"-{coins}"
                mins_coins = int(mins_coins)
                await ADD_COINS(user_id, mins_coins)
                return "LOSE"
        except Exception as e:
            string = f"ERROR, {e}"
            return string
