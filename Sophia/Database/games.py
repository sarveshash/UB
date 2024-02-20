from Sophia import GAME_DATABASE
import asyncio

db = GAME_DATABASE["Games_551"]

async def GET_AVAILABLE_USERS():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return []
    else:
        value = Find.get("USERS", [])
        return value

async def ADD_NEW_USER(user_id):
    await db.update_one({"_id": 1}, {"$addToSet": {"USERS": user_id}}, upsert=True)

async def GET_COINS_FROM_USER(user_id: int):
    USER_ACC = await GET_AVAILABLE_USERS()
    if user_id not in USER_ACC:
        return "USER_NOT_FOUND"
    string = {"_id": 2, f"{user_id}": True}  # Corrected syntax for the query
    xx = await db.find_one(string)  # Await the result
    if xx:  # Check if a document was found
        mm = int(xx["coins"])
        return mm
    else:
        return 0  # Handle case where document is not found
        
async def ADD_COINS(user_id: int, coins: int):
    # Assuming user_id is unique
    document_id = f"user_{user_id}"
    COINS_USR = await GET_COINS_FROM_USER(user_id)
    TOTAL_COINS = COINS_USR + coins
    filter = {"_id": document_id}
    update = {"$set": {"coins": TOTAL_COINS}}
    try:
        await db.insert_one({"_id": document_id, "user_id": user_id, "coins": TOTAL_COINS})
    except Exception:
        await db.update_one(filter, update)

async def REMOVE_USER(user_id):
    document_id = f"user_{user_id}"
    await db.delete_one({"_id": document_id})
    await db.update_one({"_id": 1}, {"$pull": {"USERS": user_id}})
    
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
