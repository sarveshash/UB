from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from Sophia.Database.games import *

REG_TEXT = """
**🧑‍💻 Welcome To Hyper Games ©**

**• ACCOUNT REGISTRATION 🧑‍💻**
- You need account to use Hyper Games bots.
- We Never Use Your Data's
- We Never Ask Any Details In Account Creating.
- Your Data stored in Mongodb so may Your Data will be Disappeared sometimes.
- If you send /continue Your account will be created.

**• By sending `/continue` You Agree Our Terms and Condiitions.**
"""



@Sophia.on_message(filters.command("profile", prefixes=HANDLER) & filters.group)
async def get_profile(_, message):
    LIST_USERS = await GET_AVAILABLE_USERS()
    USER_ID = message.from_user.id
    if message.reply_to_message:
        if message.reply_to_message.from_user.id in LIST_USERS:
            USER_ID = message.reply_to_message.from_user.id
        else:
            return await message.reply("The replied user don't have a account, Hyper games account is required for using this command.")
    if USER_ID in LIST_USERS:
        USER_COINS = await GET_COINS_FROM_USER(USER_ID)
        PFP = await GET_PROFILE_PIC(USER_ID)
        if PFP == None:
            await message.reply_photo("https://telegra.ph/file/a359e56250bd60eb192ff.jpg", caption=f"""
**• GAMER INFO**

**- Coins:** `{USER_COINS}`
**- Level:** `None`
**- Experience:** `None`
**- Weapons:** `None`
**- Relationship points:** `None`
**- Characters:** `None`

**•> Powered by @Hyper_Speed0™**
""")
        else:
            await message.reply_photo(PFP, caption=f"""
**• GAMER INFO**

**- Coins:** `{USER_COINS}`
**- Level:** `None`
**- Experience:** `None`
**- Weapons:** `None`
**- Relationship points:** `None`
**- Characters:** `None`

**•> Powered by @Hyper_Speed0™**
""")
    else:
        await message.reply(REG_TEXT)
        @Sophia.on_message(filters.command("continue", prefixes=HANDLER) & filters.group)
        async def create_profile(_, message):
            if message.from_user.id == USER_ID:
                await ADD_NEW_USER(USER_ID)
                await ADD_COINS(USER_ID, 1000)
                await message.reply("Thanks for creating account in Hyper Games, In this process you got 1000 coins as reward. Enjoy Have Fun")
                return

@Sophia.on_message(filters.command("profile", prefixes=HANDLER) & filters.private)
async def not_work_in_pm(_, message):
    await message.reply("This command only works on Group")
    return

@Sophia.on_message(filters.command("send", prefixes=HANDLER))
async def send_coins(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Please enter the coins to send.")
    if not message.reply_to_message:
        return await message.reply("You need reply a user to send coins")
    if message.reply_to_message.from_user.id == message.from_user.id:
        return await message.reply("You can't send coins to yourself.")
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
        return await message.reply(f"Successfully sent `{int_coins}`.")
    elif SEND_STATUS.startswith("ERROR"):
        return await message.reply(SEND_STATUS)

@Sophia.on_message(filters.command("bet", prefixes=HANDLER))
async def bet_coins(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Please enter the coins to bet.")
    coins = " ".join(message.command[1:])
    int_coins = int(coins)
    USER_ID = message.from_user.id
    BET_STATUS = await BET_COINS(USER_ID, int_coins)
    if BET_STATUS == "USER_NOT_FOUND":
        return await message.reply("You need a account to use this command")
    elif BET_STATUS == "NOT_ENOUGH_COINS":
        return await message.reply("You don't have enough coins to bet.")
    elif BET_STATUS == "NOT_POSTIVE_NUMBER":
        return await message.reply("You need enter postive integer.")
    elif BET_STATUS.startswith("ERROR"):
        return await message.reply(BET_STATUS)
    elif BET_STATUS == "BETTER_LUCK_NEXT_TIME":
        return await message.reply("**Better luck next time bruh**")
    else:
        return await message.reply(f"You won {BET_STATUS}coins")
    
@Sophia.on_message(filters.command(["setpfp", "setprofile"], prefixes=HANDLER))
async def set_pfp(_, message):
    if not message.reply_to_message.photo:
        return await message.reply("Reply to a image to set pfp")
    elif message.reply_to_message.photo:
        PIC_ID = message.reply_to_message.photo.file_id
        STATUS = await SET_PROFILE_PIC(message.from_user.id, PIC_ID)
        if STATUS == "USER_NOT_FOUND":
            return await message.reply("You need a account to use this command")
        elif STATUS == "NOT_ENOUGH_COINS":
            return await message.reply("You don't have enough coins to use this command, you need atleast 1000 coins to use this")
        elif STATUS == "SUCCESS":
            return await message.reply("Success!, I have updated your profile picture")
    else:
        return await message.reply("Please reply to a image to set your pfp")
