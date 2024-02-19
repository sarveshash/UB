from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from Sophia.Database.Games import *

@Sophia.on_message(filters.command("send", prefixes=HANDLER) & filters.user(OWNER_ID))
async def send_coins(_, message):
    users_list = await GET_AVAILABLE_USERS()
    if message.reply_to_message:
        user_id = message.from_user.id
        coins = " ".join(message.command[1:])
        int_coins = int(coins)
        user_coins_str = await GET_USER_COINS(user_id)
        user_coins = int(user_coins_str)
        if int_coins > user_coins:
            return await message.reply("You don't have enough coins")
        elif int_coins <= 0:
            return await message.reply("Enter coins in postive integer.")
        if message.reply_to_message.from_user.id in users_list:
            SEND_STATUS = await SEND_COINS(user_id, message.reply_to_message.from_user.id, int_coins)
            if SEND_STATUS == True:
                return await message.reply(f"Successfully sent {int_coins} coins")
            elif SEND_STATUS == "LOW_COINS":
                return await message.reply("You don't have enough coins")
            else:
                return await message.reply(f"Error, {SEND_STATUS}")
        else:
            return await message.reply("This user not in Hyper Games™ Database, Create a Account and try.")
    else:
        return await message.reply("You need reply a user to send coins")
            
