from pyrogram import filters
from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from config import IGNORED_USERS_ID
from Restart import restart_program
import os
import re
from time import time


Busy_stats = {}
Does_Reason_Available = {}
Busy_time = {}
Reason_Of_Busy = {}

@Sophia.on_message(filters.command(["busy", "offline", "afk"], prefixes=HANDLER) & filters.user(OWN))
async def set_into_busy(_, message):
    global Busy_stats, Does_Reason_Available, Reason_Of_Busy, Busy_time
    if len(message.command) < 2:
        Busy_stats = True
        Does_Reason_Available = False
        Reason_Of_Busy = None
    else:
        Busy_stats = True
        Does_Reason_Available = True
        Reason_Of_Busy = " ".join(message.command[1:])
    if Does_Reason_Available == False:
        Busy_time['start'] = time()
        await message.reply_text("**Master**, I Set You In Offline Mode I will Reply to everyone who wants to talk you, bye 👋")
    else:
        Busy_time['start'] = time()
        await message.reply_text(f"**UwU**, I Have set you In offline mode successfully ✅\n**Reason:** `{Reason_Of_Busy}`")
    if Busy_stats == True:
        @Sophia.on_message(filters.private & ~filters.user(OWN))
        async def say_master_is_busy(_, message):
            elapsed_time_seconds = round(time() - Busy_time['start'])
            # Convert seconds to hours, minutes, and seconds 
            hours, remainder = divmod(elapsed_time_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            # Format the result
            formatted_elapsed_time = f"{hours}h {minutes}m {seconds}s"
            if message.from_user.id == IGNORED_USERS_ID:
                print(" ")
            if Does_Reason_Available == True:
                await message.reply_text(f"**Sorry**, My Master is Currently Offline ❌\n**Because**: `{Reason_Of_Busy}`\n\n**I haven't seen my Master since:** `{formatted_elapsed_time}`")
            else:
                await message.reply_text(f"**Sorry**, My **Master** is Currently In Offline Can you Come Later?\n\n**I haven't seen my Master since:** `{formatted_elapsed_time}`")
        @Sophia.on_message(filters.user(OWN))
        async def remove_busy_mode(_, message):
            from Sophia.plugins.Spam import what_is_text as TXT_FROM_SPAM
            if message.text == "Sᴏʀʀʏ, Yᴏᴜ ᴀʀᴇ ɪɢɴᴏʀᴇᴅ ʙʏ ᴍʏ ʟᴏᴠᴇʟʏ ❤️ Mᴀsᴛᴇʀ, ɪғ ʏᴏᴜ sᴇɴᴅ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴀɢᴀɪɴ ʏᴏᴜ ᴡɪʟʟ ʙᴇ ɢᴇᴛ Bʟᴏᴄᴋᴇᴅ." or message.text == "This is your second warning. If you send another message, you will be blocked." or message.text == "Sorry, You Have Breaked Your Limits that's why I blocked You!" or message.text == TXT_FROM_SPAM:
                print(" ")
            elif message.text.startswith("Master, I have Been Blocked A user From Ignored"):
                print(" ")
            else:
                await message.reply_text("**Hello**, Master Welcome Back! 🥀")
                await restart_program()
