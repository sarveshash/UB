from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from Sophia.Database.games import *

PROFILE_TEXT = """
**🧑‍💻 Welcome To Hyper Games ©**

**• ACCOUNT REGISTRATION 🧑‍💻**
- You need account to use Hyper Games bots.
- We Never Use Your Data's
- We Never Ask Any Details In Account Creating.
- Your Data stored in Mongodb so may Your Data will be Disappeared sometimes.
- If you send /continue Your account will be created.

**• By sending `/continue` You Agree Our Terms and Condiitions.**
"""

USER_ID = 0
@Sophia.on_message(filters.command("profile", prefixes=HANDLER) & filters.group)
async def get_profile(_, message):
    global USER_ID
    LIST_USERS = await GET_AVAILABLE_USERS()
    USER_ID = message.from_user.id
    if USER_ID in LIST_USERS:
        USER_COINS = await GET_COINS_FROM_USER(USER_ID)
        await message.reply(f"You have {USER_COINS} coins")
    else:
        await message.reply(PROFILE_TEXT)
        @Sophia.on_message(filters.command("continue", prefixes=HANDLER) & filters.group)
        async def create_profile(_, message):
            global USER_ID
            if message.from_user.id == USER_ID:
                await ADD_NEW_USER(USER_ID)
                await ADD_COINS(USER_ID, 1000)
                await message.reply("Thanks for creating account in Hyper Games, In this process you got 1000 coins as reward. Enjoy Have Fun")
                return

@Sophia.on_message(filters.command("profile", prefixes=HANDLER) & filters.private)
async def not_work_in_pm(_, message):
    await message.reply("This command only works on Group")
    return

@Sophia.on_message(filters.command("send", prefixes=HANDLER) & filters.reply)
async def send_coins(_, message):
    if len(message.command) < 2:
        return await message.reply_text("➲ Master, Please enter the coins to send.")
    coins = " ".join(message.command[1:])
    int_coins = int(coins)
    REPLY_USR = message.reply_to_message.from_user.id
    USER_ID = message.from_user.id
    SEND_STATUS = await SEND_COINS(USER_ID, REPLY_USR, int_coins)
    if SEND_STATUS == "FROM_USER_NOT_FOUND":
        return await message.reply("You need a account to use this command")
    elif SEND_STATUS == "TO_USER_NOT_FOUND":
        return await message.reply("Replied user don't have a account, account is required for using this command")
    elif SEND_STATUS == "NOT_ENOUGH_COINS":
        return await message.reply("You don't have enough Coins to send.")
    elif SEND_STATUS == "NOT_POSTIVE_NUMBER":
        return await message.reply("You need enter postive integer.")
    elif SEND_STATUS == "SUCCESS":
        return await message.reply(f"Successfully sent {int_coins}")
    elif SEND_STATUS.startswith("ERROR"):
        return await message.reply(SEND_STATUS)
