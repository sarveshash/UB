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
        await message.reply("WAIT")
    else:
        await message.reply(PROFILE_TEXT)
        @Sophia.on_message(filters.command("continue", prefixes=HANDLER) & filters.group)
        async def create_profile(_, message):
            global USER_ID
            if message.from_user.id == USER_ID:
                await ADD_NEW_USER(USER_ID)
                await message.reply("Thanks for creating account in Hyper Games, In this process you got 1000 coins as reward. Enjoy Have Fun")
                return
