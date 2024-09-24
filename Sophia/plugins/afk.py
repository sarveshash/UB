from pyrogram import filters
from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from config import BOTS_ALLOWED_TO_WORK_IN_BUSY_COMMANDS
from Restart import restart_program
import os
import re
from datetime import datetime
from Sophia.Database.afk import *
from Sophia.Database.ignore_users import *
from Sophia.Database.backup_msg import *

def calculate_time(start_time, end_time):
    ping_time = (end_time - start_time).total_seconds() * 1000
    uptime = (end_time - start_time).total_seconds()
    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)
    END = f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
    return END

async def denied_users(_, client, update):
    if not await GET_AFK():
        return False
    else:
        ignore_class = IGNORED_USERS()
        IGNORED_USERS_ID = await ignore_class.GET()
        if update.chat.id in IGNORED_USERS_ID:
            return False
        return True

@Sophia.on_message(filters.command(["busy", "offline", "afk"], prefixes=HANDLER) & filters.user(OWN))
async def set_afk(_, message):
    Busy_time = datetime.now()
    if len(message.command) < 2:
        await SET_AFK(Busy_time, None)
        await message.reply_text("➲ Master, I successfully Set you AFK mode, I will reply to everyone if anyone chats you.")
    else:
        Reason_Of_Busy = " ".join(message.command[1:])
        await SET_AFK(Busy_time, Reason_Of_Busy)
        await message.reply_text(f"➲ I have Set you in AFK mode successfully ✅\n**Reason:** `{Reason_Of_Busy}`")
    
@Sophia.on_message(filters.private & filters.create(denied_users) & filters.incoming & ~filters.service & ~filters.me & ~filters.bot)
async def say_afk(_, message):
    try:
        Busy_time = await GET_AFK_TIME()
        formatted_elapsed_time = calculate_time(Busy_time, datetime.now())
        reason = await GET_AFK_REASON()
        if reason == None:
            await message.reply_text(f"**⚠️ OFFLINE WARNING ⚠️**\n\nSorry, My master is Currently Offline, You can't chat with my master currently now. and don't spam here because he/she maybe in a highly stress or maybe he/she in a work or he/she in a problem anything but don't distrub him/her now please.\n\n**➲ Reason: NOT SET\n➲ Offline Duration:** {formatted_elapsed_time}")
        else:
            await message.reply_text(f"**⚠️ OFFLINE WARNING ⚠️**\n\nSorry, My master is Currently Offline, You can't chat with my master currently now. and don't spam here because he/she maybe in a highly stress or maybe he/she in a work or he/she in a problem anything but don't distrub him/her now please.\n\n**➲ Reason: `{Reason_Of_Busy}`\n➲ Offline Duration:** {formatted_elapsed_time}")
        await Sophia.mark_chat_unread(message.chat.id)
        if await GET_BACKUP():
            backup_chat = await GET_BACKUP_CHANNEL_ID(message.chat.id)
            try:
                await Sophia.forward_messages(backup_chat, message.chat.id, message.id)
            except Exception as e:
                if str(e) == """Telegram says: [400 CHANNEL_INVALID] - The channel parameter is invalid (caused by "channels.GetChannels")""":
                    chat = await Sophia.create_channel(f"{message.chat.first_name} BACKUP", "~ @Hyper_Speed0")
                    await ADD_BACKUP_CHAT(message.chat.id)
                    await SET_BACKUP_CHANNEL_ID(message.chat.id, chat.id)
                    await Sophia.forward_messages(chat.id, message.chat.id, message.id)
                    await Sophia.archive_chats(chat.id)
                    return
                else:
                    print(f"Error on afk.py when backuping message {message.chat.id}: {str(e)}")
    except Exception as e:
        raise Exception(e)
    
@Sophia.on_message(filters.group & ~filters.user(OWN) & filters.create(denied_users))
async def Group_say_master_offline(_, message):
    Busy_time = await GET_AFK_TIME()
    formatted_elapsed_time = calculate_time(Busy_time, datetime.now())
    if message.reply_to_message.from_user.id == OWN:
        Reason_Of_Busy = await GET_AFK_REASON()
        if Reason_Of_Busy == None:
            await message.reply_text(f"**⚠️ OFFLINE WARNING ⚠️**\n\nSorry, My master is Currently Offline, You can't chat with my master currently now. and don't spam here because he/she maybe in a highly stress or maybe he/she in a work or he/she in a problem anything but don't distrub him/her now please.\n\n**➲ Reason: NOT SET\n➲ Offline Duration:** {formatted_elapsed_time}")
        else:
            await message.reply_text(f"**⚠️ OFFLINE WARNING ⚠️**\n\nSorry, My master is Currently Offline, You can't chat with my master currently now. and don't spam here because he/she maybe in a highly stress or maybe he/she in a work or he/she in a problem anything but don't distrub him/her now please.\n\n**➲ Reason: `{Reason_Of_Busy}`\n➲ Offline Duration:** {formatted_elapsed_time}")
        await Sophia.mark_chat_unread(message.chat.id)
    
@Sophia.on_message(filters.user(OWN) & filters.create(denied_users))
async def remove_busy_mode(_, message):
    Busy_time = await GET_AFK_TIME()
    formatted_elapsed_time = calculate_time(Busy_time, datetime.now())
    await UNSET_AFK()
    await message.reply_text(f"➲ **Hello**, Master Welcome Again ✨🥀.\n➲ **Your Offline Duration**: `{formatted_elapsed_time}`🥺")
