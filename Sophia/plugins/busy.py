from pyrogram import filters
from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from config import IGNORED_USERS_ID, BOTS_ALLOWED_TO_WORK_IN_BUSY_COMMANDS
from Restart import restart_program
import os
import re
from time import time
from Sophia.Database.afk import *

Busy_stats = {}
Does_Reason_Available = {}
Busy_time = {}
Reason_Of_Busy = {}

@Sophia.on_message(filters.command(["busy", "offline", "afk"], prefixes=HANDLER) & filters.user(OWN))
async def set_into_busy(_, message):
    global Busy_stats, Does_Reason_Available, Reason_Of_Busy, Busy_time
    if len(message.command) < 2:
        Busy_time = time()
        await SET_AFK(Busy_time, None)
        await message.reply_text("➲ Master, I successfully Set you AFK mode, I will reply to everyone if anyone chats you.")
    else:
        Reason_Of_Busy = " ".join(message.command[1:])
        Busy_time = time()
        await SET_AFK(Busy_time, Reason_Of_Busy)
        await message.reply_text(f"➲ I have Set you in AFK mode successfully ✅\n**Reason:** `{Reason_Of_Busy}`")

SIGMA = GET_AFK()
if SIGMA:
    @Sophia.on_message(filters.private & ~filters.user(OWN))
    async def say_master_is_busy(_, message):
        Busy_time = GET_AFK_TIME()
        elapsed_time_seconds = round(time() - Busy_time)
        hours, remainder = divmod(elapsed_time_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_elapsed_time = f"{hours}h {minutes}m {seconds}s"
        if message.from_user.id in IGNORED_USERS_ID:
            return
        if BOTS_ALLOWED_TO_WORK_IN_BUSY_COMMANDS == False:
            if message.from_user.is_bot:
                return
        Reason_Of_Busy = GET_AFK_REASON()
        if not Reason == None:
            await message.reply_text(f"**⚠️ OFFLINE WARNING ⚠️**\n\nSorry, My master is Currently Offline, You can't chat with my master currently now. and don't spam here because he/she maybe in a highly stress or maybe he/she in a work or he/she in a problem anything but don't distrub him/her now please.\n\n**➲ Reason: `{Reason_Of_Busy}`\n➲ Offline Duration:** {formatted_elapsed_time}")
        else:
            await message.reply_text(f"**⚠️ OFFLINE WARNING ⚠️**\n\nSorry, My master is Currently Offline, You can't chat with my master currently now. and don't spam here because he/she maybe in a highly stress or maybe he/she in a work or he/she in a problem anything but don't distrub him/her now please.\n\n**➲ Reason: NOT SET\n➲ Offline Duration:** {formatted_elapsed_time}")
        @Sophia.on_message(filters.group & ~filters.user(OWN))
        async def Group_say_master_offline(_, message):
            info = await Sophia.get_users(OWN)
            username = info.username
            msg = message.text
            if message.from_user.id in IGNORED_USERS_ID:
                return
            elapsed_time_seconds = round(time() - Busy_time['start'])
            hours, remainder = divmod(elapsed_time_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            formatted_elapsed_time = f"{hours}h {minutes}m {seconds}s"
            if message.reply_to_message.from_user.id == OWN:
                if Does_Reason_Available == True:
                    await message.reply_text(f"**⚠️ OFFLINE WARNING ⚠️**\n\nSorry, My master is Currently Offline, You can't chat with my master currently now. and don't spam here because he/she maybe in a highly stress or maybe he/she in a work or he/she in a problem anything but don't distrub him/her now please.\n\n**➲ Reason: `{Reason_Of_Busy}`\n➲ Offline Duration:** {formatted_elapsed_time}")
                else:
                    await message.reply_text(f"**⚠️ OFFLINE WARNING ⚠️**\n\nSorry, My master is Currently Offline, You can't chat with my master currently now. and don't spam here because he/she maybe in a highly stress or maybe he/she in a work or he/she in a problem anything but don't distrub him/her now please.\n\n**➲ Reason: NOT SET\n➲ Offline Duration:** {formatted_elapsed_time}")
@Sophia.on_message(filters.user(OWN))
        async def remove_busy_mode(_, message):
            elapsed_time_seconds = round(time() - Busy_time['start'])
            # Convert seconds to hours, minutes, and seconds 
            hours, remainder = divmod(elapsed_time_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            # Format the result
            formatted_elapsed_time = f"{hours}h {minutes}m {seconds}s"
            from Sophia.plugins.Spam import what_is_text as TXT_FROM_SPAM
            if message.text == "Sᴏʀʀʏ, Yᴏᴜ ᴀʀᴇ ɪɢɴᴏʀᴇᴅ ʙʏ ᴍʏ ʟᴏᴠᴇʟʏ ❤️ Mᴀsᴛᴇʀ, ɪғ ʏᴏᴜ sᴇɴᴅ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴀɢᴀɪɴ ʏᴏᴜ ᴡɪʟʟ ʙᴇ ɢᴇᴛ Bʟᴏᴄᴋᴇᴅ." or message.text == "This is your second warning. If you send another message, you will be blocked." or message.text == "Sorry, You Have Breaked Your Limits that's why I blocked You!" or message.text == TXT_FROM_SPAM:
                print(" ")
            elif message.text.startswith("Master, I have Been Blocked A user From Ignored"):
                print(" ")
            else:
                await message.reply_text(f"➲ **Hello**, Master Welcome Again ✨🥀.\n➲ **Your Offline Duration**: `{formatted_elapsed_time}`🥺")
                await restart_program()
