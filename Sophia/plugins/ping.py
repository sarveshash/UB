# This Codes We take from https://github.com/otazuki004/QuantumRobot.git
# Please use QuantumRobot

from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
from pyrogram import *
import asyncio
import os
import requests
from datetime import datetime
import time

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

@bot.on_message(filters.command("ping", prefixes=HANDLER) & filters.user(OWNER_ID))
def ping_pong(client, message):
    # Calculate the bot's response time
    start_time = bot_start_time
    end_time = datetime.now()

    # Calculate the round-trip time
    ping_time = (end_time - start_time).total_seconds() * 1000

    # Calculate the bot's uptime
    uptime = (end_time - bot_start_time).total_seconds()
    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Send the ping-pong message with uptime
    message.reply_text(f"» Pᴏɴɢ! Rᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ: {ping_website(telegram_url)}\n» Uᴘᴛɪᴍᴇ: {int(hours)}h {int(minutes)}m {int(seconds)}s")
