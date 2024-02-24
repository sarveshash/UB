# This Codes We take from https://github.com/otazuki004/QuantumRobot.git
# Please use QuantumRobot

from Sophia import HANDLER
from Sophia.__main__ import Sophia as bot
from config import OWNER_ID
from config import SUDO_USERS_ID
from pyrogram import filters
from pyrogram import *
import asyncio
import os
import requests
from datetime import datetime
import time
from Sophia.Database.Broadcast import *
from pyrogram import enums

def ping_website(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        if response.status_code == 200:
            response_time_ms = (end_time - start_time) * 1000
            return f"{response_time_ms:.2f}ms"
        else:
            return f"Failed to ping {url}. Status code: {response.status_code}"

    except requests.ConnectionError:
        return f"» Failed to connect to {url}"

# Example: Ping Telegram's website
telegram_url = "https://google.com"

bot_start_time = datetime.now()

@bot.on_message(filters.command("ping", prefixes=HANDLER))
def ping_pong(client, message):
    if not message.from_user.id == OWNER_ID or message.from_user.id in SUDO_USERS_ID:
        return
    CHATS = GET_ALL_CHATS()
    if not message.chat.id == OWNER_ID:
        if message.chat.id not in CHATS:
            if not message.chat.type == enums.ChatType.BOT:
                if message.chat.type == enums.ChatType.SUPERGROUP:
                    ADD_ANY_CHAT_ID(message.chat.id)
                    ADD_GROUP_ID(message.chat.id)
                elif message.chat.type == enums.ChatType.PRIVATE:
                    ADD_ANY_CHAT_ID(message.chat.id)
                    ADD_USER_ID(message.chat.id)
                
    # Calculate the bot's response time
    start_time = bot_start_time
    end_time = datetime.now()
    ping_time = (end_time - start_time).total_seconds() * 1000
    uptime = (end_time - bot_start_time).total_seconds()
    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)
    message.reply_text(f"» Pᴏɴɢ! Rᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ: {ping_website(telegram_url)}\n» Uᴘᴛɪᴍᴇ: {int(hours)}h {int(minutes)}m {int(seconds)}s")
