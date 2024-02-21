from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from Sophia.Database.games import *
from pyrogram import enums
import random
from Restart import restart_program

async def CHOICE_GEN(user_one: int, user_one_lvl: int, user_two: int, user_two_lvl: int):
    if user_one_lvl > user_two_lvl:
        if user_one_lvl < 3:
            chance = 0.5
        elif user_one_lvl < 7:
            chance = 0.33
        elif user_one_lvl < 16:
            chance = 0.4
        elif user_one_lvl < 25:
            chance = 0.43
        elif user_one_lvl < 38:
            chance = 0.47
        elif user_one_lvl < 50:
            chance = 0.45
        elif user_one_lvl < 75:
            chance = 0.53
        elif user_one_lvl < 100:
            chance = 0.5
        else:
            chance = 0.65
        RAN_CHOICE = random.random()
        return user_two if RAN_CHOICE < chance else user_one
    else:
        user_one_lvl = user_two_lvl 
        user_two_lvl = user_one_lvl
        if user_one_lvl < 3:
            chance = 0.5
        elif user_one_lvl < 7:
            chance = 0.33
        elif user_one_lvl < 16:
            chance = 0.4
        elif user_one_lvl < 25:
            chance = 0.43
        elif user_one_lvl < 38:
            chance = 0.47
        elif user_one_lvl < 50:
            chance = 0.45
        elif user_one_lvl < 75:
            chance = 0.53
        elif user_one_lvl < 100:
            chance = 0.5
        else:
            chance = 0.90
        RAN_CHOICE = random.random()
        return user_one if RAN_CHOICE < chance else user_two

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



@Sophia.on_message(filters.command("profile", prefixes=HANDLER))
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
        EXP = await GET_EXP(USER_ID)
        NAME = await GET_USER_NAME(USER_ID)
        LEVEL = await GET_LEVEL(USER_ID)
        if PFP == None:
            await message.reply_photo("https://telegra.ph/file/a359e56250bd60eb192ff.jpg", caption=f"""
**• GAMER INFO**

**- Name:** {NAME}
**- ID:** `{USER_ID}`
**- Coins:** `{USER_COINS}`
**- Level:** `{LEVEL}`
**- Experience:** `{EXP}`
**- Weapons:** `None`
**- Relationship points:** `None`
**- Characters:** `None`

**•> Powered by @Hyper_Speed0™**
""")
        else:
            await message.reply_photo(PFP, caption=f"""
**• GAMER INFO**

**- Name:** {NAME}
**- ID:** {USER_ID}
**- Coins:** `{USER_COINS}`
**- Level:** `{LEVEL}`
**- Experience:** `{EXP}`
**- Weapons:** `None`
**- Relationship points:** `None`
**- Characters:** `None`

**•> Powered by @Hyper_Speed0™**
""")
    else:
        if message.chat.type == enums.ChatType.PRIVATE:
            return await message.reply("Creating account only works on group.")
        await message.reply(REG_TEXT)
        @Sophia.on_message(filters.command("continue", prefixes=HANDLER) & filters.group)
        async def create_profile(_, message):
            if message.from_user.id == USER_ID:
                await ADD_NEW_USER(USER_ID)
                await ADD_COINS(USER_ID, 1000)
                await message.reply("Thanks for creating account in Hyper Games, In this process you got 1000 coins as reward. Enjoy Have Fun")
                await restart_program()
                return

@Sophia.on_message(filters.command(["send", "sent", "transfer"], prefixes=HANDLER))
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
    elif BET_STATUS == "LOSE":
        return await message.reply(f"You lose {int_coins}.")
    elif BET_STATUS == "PRO":
        return await message.reply(f"Pro bet, you won {int_coins*2}")
    else:
        return await message.reply(f"You won {BET_STATUS} coins")
    
@Sophia.on_message(filters.command(["setpfp", "setprofile"], prefixes=HANDLER))
async def set_pfp(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Please enter your image link to set.")
    IMAGE_LINK = " ".join(message.command[1:])
    if IMAGE_LINK.startswith("https://"):
        STATUS = await SET_PROFILE_PIC(message.from_user.id, IMAGE_LINK)
        if STATUS == "USER_NOT_FOUND":
            return await message.reply("You need a account to use this command.")
        elif STATUS == "NOT_ENOUGH_COINS":
            return await message.reply("You don't have enough coins to use this command, you need atleast 1000 coins to use this")
        elif STATUS == "SUCCESS":
            return await message.reply("Success!, I have updated your profile picture")
    else:
        return await message.reply("Please enter a valid image link to set.")

@Sophia.on_message(filters.command(["setname", "setnewname"], prefixes=HANDLER))
async def set_name(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Please enter your new name to set.")
    NAME_NEW = " ".join(message.command[1:])
    STATUS = await SET_USER_NAME(message.from_user.id, NAME_NEW)
    if STATUS == "USER_NOT_FOUND":
        return await message.reply("You need a account to use this command")
    elif STATUS == "NOT_ENOUGH_COINS":
        return await message.reply("You don't have enough coins to use this command, you need atleast 1999 coins to use this")
    elif STATUS == "SUCCESS":
        return await message.reply("Success!, I have updated your profile name")
        


@Sophia.on_message(filters.command("fight", prefixes=HANDLER))
async def fight(_, message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == message.from_user.id:
            return await message.reply("How you can fight to yourself?")
        LIST_USERS = await GET_AVAILABLE_USERS()
        REPLY_USER = message.reply_to_message.from_user.id
        USER_ID = message.from_user.id
        COINS_RPL_USR = await GET_COINS_FROM_USER(REPLY_USER)
        COINS_FR_USR = await GET_COINS_FROM_USER(USER_ID)
        if USER_ID not in LIST_USERS:
            return await message.reply("You need a account to use this command")
        elif REPLY_USER not in LIST_USERS:
            return await message.reply("Replied user don't have account, account is required to use this command.")
        elif COINS_RPL_USR < 500:
            return await message.reply("Replied user need atleast 500 coins to fight")
        elif COINS_FR_USR < 500:
            return await message.reply("You Need atleast 500 coins to fight")
        FIGHT = await message.reply("Fight started")
        await asyncio.sleep(1)
        await FIGHT.edit("•")
        await asyncio.sleep(1)
        await FIGHT.edit("••")
        await asyncio.sleep(0.6)
        await FIGHT.edit("•••")
        await asyncio.sleep(0.6)
        FR_FIRST_NAME = message.from_user.first_name
        RP_FIRST_NAME = message.reply_to_message.from_user.first_name
        FR_USR_LVL = await GET_LEVEL(USER_ID)
        RPL_USR_LVL = await GET_LEVEL(REPLY_USER)
        RAN_CHOICE = await CHOICE_GEN(USER_ID, FR_USR_LVL, REPLY_USER, RPL_USR_LVL)
        if RAN_CHOICE == USER_ID:
            SEND = await SEND_COINS(REPLY_USER, USER_ID, 500)
            if SEND == "SUCCESS":
                return await FIGHT.edit(f"Fight was so interesting but winer is {FR_FIRST_NAME} got 500 coins from {RP_FIRST_NAME}")
        else:
            SEND = await SEND_COINS(USER_ID, REPLY_USER, 500)
            if SEND == "SUCCESS":
                return await FIGHT.edit(f"Fight was so interesting but winer is {RP_FIRST_NAME} got 500 coins from {FR_FIRST_NAME}")
    else:
        return await message.reply("Please reply a user to fight.")
