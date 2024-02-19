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
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.from_user.id
        coins = " ".join(message.command[1:])
        try:
            int_coins = int(coins)
        except ValueError:
            return await message.reply("Enter coins in positive integer.")
        
        if int_coins <= 0:
            return await message.reply("Enter coins in positive integer.")
        
        user_coins_str = await GET_USER_COINS(user_id)
        
        if user_coins_str is None:
            return await message.reply("You are not registered in the Hyper Games™ Database. Create an account to receive coins.")
        
        user_coins = int(user_coins_str)
        
        if int_coins > user_coins:
            return await message.reply("You don't have enough coins.")
        
        recipient_id = message.reply_to_message.from_user.id
        
        if recipient_id not in users_list:
            return await message.reply("The recipient is not registered in the Hyper Games™ Database. Ask them to create an account to receive coins.")
        
        send_status = await SEND_COINS(user_id, recipient_id, int_coins)
        
        if send_status is True:
            return await message.reply(f"Successfully sent {int_coins} coins.")
        elif send_status == "LOW_COINS":
            return await message.reply("You don't have enough coins.")
        else:
            return await message.reply(f"Error: {send_status}")
    else:
        return await message.reply("You need to reply to a user to send coins.")
