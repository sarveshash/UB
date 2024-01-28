from pyrogram import filters
from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from config import IGNORED_USERS_ID
from Restart import restart_program
import os
import re


Busy_stats = {}


@Sophia.on_message(filters.command(["busy", "offline", "afk"], prefixes=HANDLER) & filters.user(OWN))
async def set_into_busy(_, message):
    global Busy_stats
    Busy_stats = True
    await message.reply_text("💖 **Master**, I Set You In Offline Mode I will Reply to everyone who wants to talk you, bye 👋")
    if Busy_stats == True:
        @Sophia.on_message(filters.private & ~filters.user(OWN))
        async def say_master_is_busy(_, message):
            if message.from_user.id == IGNORED_USERS_ID:
                return
            await message.reply_text("**Sorry**, My **Master** is Currently In Offline Can you Come Later?")
        @Sophia.on_message(filters.regex("Otazuki") ~filters.user(OWN) & filters.group)
        async def say_master_busy_in_Group(_, message):
            if message.from_user.id == IGNORED_USERS_ID:
                return
            await message.reply_text("**Sorry**, My **Master** is Currently In Offline Can you Come Later?")
        @Sophia.on_message(filters.user(OWN))
        async def remove_busy_mode(_, message):
            if message.text == "Sᴏʀʀʏ, Yᴏᴜ ᴀʀᴇ ɪɢɴᴏʀᴇᴅ ʙʏ ᴍʏ ʟᴏᴠᴇʟʏ ❤️ Mᴀsᴛᴇʀ, ɪғ ʏᴏᴜ sᴇɴᴅ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴀɢᴀɪɴ ʏᴏᴜ ᴡɪʟʟ ʙᴇ ɢᴇᴛ Bʟᴏᴄᴋᴇᴅ." or message.text == "This is your second warning. If you send another message, you will be blocked." or message.text == "Sorry, You Have Breaked Your Limits that's why I blocked You!":
                return
            elif message.text.startswith("Master, I have Been Blocked A user From Ignored"):
                return
            await message.reply_text("**Hi Master**, Welcome Back! 🥀")
            await restart_program()
