from pyrogram import filters
from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from config import IGNORED_USERS_ID, BOTS_ALLOWED_TO_WORK_IN_BUSY_COMMANDS
from Restart import restart_program
import os
import re
from datetime import datetime
from Sophia.Database.afk import *

def calculate_time(start_time, end_time):
    ping_time = (end_time - start_time).total_seconds() * 1000
    uptime = (end_time - start_time).total_seconds()
    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)
    END = f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
    return END


@Sophia.on_message(filters.command(["busy", "offline", "afk"], prefixes=HANDLER) & filters.user(OWN))
async def set_into_busy(_, message):
    Busy_time = datetime.now()
    if len(message.command) < 2:
        await SET_AFK(Busy_time, None)
        await message.reply_text("➲ Master, I successfully Set you AFK mode, I will reply to everyone if anyone chats you.")
    else:
        Reason_Of_Busy = " ".join(message.command[1:])
        await SET_AFK(Busy_time, Reason_Of_Busy)
        await message.reply_text(f"➲ I have Set you in AFK mode successfully ✅\n**Reason:** `{Reason_Of_Busy}`")
    @Sophia.on_message(filters.private & ~filters.user(OWN))
    async def say_master_is_busy(_, message):
        Busy_time = await GET_AFK_TIME()
        formatted_elapsed_time = calculate_time(Busy_time, datetime.now())
        if message.from_user.id in IGNORED_USERS_ID:
            return
        if BOTS_ALLOWED_TO_WORK_IN_BUSY_COMMANDS:
            if message.from_user.is_bot:
                return
        Reason_Of_Busy = await GET_AFK_REASON()
        if Reason_Of_Busy == None:
            await message.reply_text(f"**⚠️ OFFLINE WARNING ⚠️**\n\nSorry, My master is Currently Offline, You can't chat with my master currently now. and don't spam here because he/she maybe in a highly stress or maybe he/she in a work or he/she in a problem anything but don't distrub him/her now please.\n\n**➲ Reason: NOT SET\n➲ Offline Duration:** {formatted_elapsed_time}")
        else:
            await message.reply_text(f"**⚠️ OFFLINE WARNING ⚠️**\n\nSorry, My master is Currently Offline, You can't chat with my master currently now. and don't spam here because he/she maybe in a highly stress or maybe he/she in a work or he/she in a problem anything but don't distrub him/her now please.\n\n**➲ Reason: `{Reason_Of_Busy}`\n➲ Offline Duration:** {formatted_elapsed_time}")
    @Sophia.on_message(filters.group & ~filters.user(OWN))
    async def Group_say_master_offline(_, message):
        if message.from_user.id in IGNORED_USERS_ID:
            return
        Busy_time = await GET_AFK_TIME()
        formatted_elapsed_time = calculate_time(Busy_time, datetime.now())
        if message.reply_to_message.from_user.id == OWN:
            Reason_Of_Busy = await GET_AFK_REASON()
            if Reason_Of_Busy == None:
                await message.reply_text(f"**⚠️ OFFLINE WARNING ⚠️**\n\nSorry, My master is Currently Offline, You can't chat with my master currently now. and don't spam here because he/she maybe in a highly stress or maybe he/she in a work or he/she in a problem anything but don't distrub him/her now please.\n\n**➲ Reason: NOT SET\n➲ Offline Duration:** {formatted_elapsed_time}")
            else:
                await message.reply_text(f"**⚠️ OFFLINE WARNING ⚠️**\n\nSorry, My master is Currently Offline, You can't chat with my master currently now. and don't spam here because he/she maybe in a highly stress or maybe he/she in a work or he/she in a problem anything but don't distrub him/her now please.\n\n**➲ Reason: `{Reason_Of_Busy}`\n➲ Offline Duration:** {formatted_elapsed_time}")
    @Sophia.on_message(filters.user(OWN))
    async def remove_busy_mode(_, message):
        Busy_time = await GET_AFK_TIME()
        formatted_elapsed_time = calculate_time(Busy_time, datetime.now())
        await UNSET_AFK()
        await message.reply_text(f"➲ **Hello**, Master Welcome Again ✨🥀.\n➲ **Your Offline Duration**: `{formatted_elapsed_time}`🥺")
        await restart_program()
