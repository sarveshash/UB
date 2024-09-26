from Sophia import *
from pyrogram import *
from Sophia.Database.afk import *
from Sophia.Database.ignore_users import *
from Sophia.Database.backup_msg import *
from Sophia.Database.pmguard import *
from pyrogram.enums import *
from config import OWNER_ID
from datetime import datetime
import os
import re
import asyncio

def calculate_time(start_time, end_time):
    ping_time = (end_time - start_time).total_seconds() * 1000
    uptime = (end_time - start_time).total_seconds()
    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)
    time = f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
    return time

warning_count = {}

async def filter_(_, client, update):
    message = update
    if await GET_BACKUP():  # Backup section
        command = False
        if update.from_user.id == OWNER_ID:
            if update.text:
                if update.text.startswith(tuple(HANDLER)) and not len(update.text) < 2:
                    command = True
        if not command and update.chat.id not in await GET_STOP_BACKUP_CHATS() and update.chat.id != OWNER_ID:
            CHATS = await GET_BACKUP_CHATS()
            if update.chat.id in CHATS:
                chat_id = await GET_BACKUP_CHANNEL_ID(update.chat.id)
                try:
                    if message.chat.type != ChatType.PRIVATE and not message.text and message.chat.type != ChatType.CHANNEL and await GET_BACKUP(group=True):
                        await Sophia.forward_messages(chat_id, message.chat.id, message.id)
                    elif message.chat.type == ChatType.PRIVATE:
                        await Sophia.forward_messages(chat_id, message.chat.id, message.id)
                except Exception as e:
                    await Sophia.send_message(OWNER_ID, f"Error in forwarding messages: {str(e)}")
                    if message.chat.first_name != None:
                        c_name = f"{message.chat.first_name} BACKUP"
                    else:
                        c_name = f"{message.chat.title} GROUP BACKUP"
                    if message.chat.username:
                        chat = await Sophia.create_channel(f"{c_name}", f"Username: @{message.chat.username}\n\n~ @Hyper_Speed0")
                    else:
                        chat = await Sophia.create_channel(f"{c_name}", "~ @Hyper_Speed0")
                    await ADD_BACKUP_CHAT(message.chat.id)
                    await SET_BACKUP_CHANNEL_ID(message.chat.id, chat.id)
                    if message.chat.type != ChatType.PRIVATE and not message.text and message.chat.type != ChatType.CHANNEL and await GET_BACKUP(group=True):
                        await Sophia.forward_messages(chat.id, message.chat.id, message.id)
                    elif message.chat.type == ChatType.PRIVATE:
                        await Sophia.forward_messages(chat_id, message.chat.id, message.id)
                    await Sophia.archive_chats(chat.id)
            else:
                try:
                    if message.chat.first_name != None:
                        c_name = f"{message.chat.first_name} BACKUP"
                    else:
                        c_name = f"{message.chat.title} GROUP BACKUP"
                    if message.chat.username:
                        chat = await Sophia.create_channel(f"{c_name}", f"Username: @{message.chat.username}\n\n~ @Hyper_Speed0")
                    else:
                        chat = await Sophia.create_channel(f"{c_name}", "~ @Hyper_Speed0")
                    await ADD_BACKUP_CHAT(message.chat.id)
                    await SET_BACKUP_CHANNEL_ID(message.chat.id, chat.id)
                    if message.chat.type != ChatType.PRIVATE and not message.text and message.chat.type != ChatType.CHANNEL and await GET_BACKUP(group=True):
                        await Sophia.forward_messages(chat.id, message.chat.id, message.id)
                    elif message.chat.type == ChatType.PRIVATE:
                        await Sophia.forward_messages(chat_id, message.chat.id, message.id)
                    await Sophia.archive_chats(chat.id)
                except Exception as e:
                    print(e)

    if await GET_PM_GUARD() and update.chat.id not in (await GET_APPROVED_USERS()) and message.chat.type == ChatType.PRIVATE and message.from_user.id != OWNER_ID:
        user_id = message.chat.id
        global warning_count
        maximum_message_count = await GET_WARNING_COUNT()
        if user_id not in warning_count:
            warning_count[user_id] = 0
        warning_count[user_id] += 1
        if warning_count[user_id] < maximum_message_count:
            await message.reply(f"**⚠️ WARNING**\n\nSorry, my master has enabled the PmGuard feature. You can't send messages until my master approves you or disables this feature. If you Spam Here or the warning exceeds the limits I will Block You.\n\n**➲ Warning Counts** `{warning_count[user_id]}/{maximum_message_count}`")
        elif warning_count[user_id] >= maximum_message_count:
            try:
                await message.reply("➲ You have exceeded your limits, so I have blocked you!")
                await Sophia.block_user(user_id)
            except Exception as e:
                print(e)
                await Sophia.send_message(OWNER_ID, f"Error in blocking user: {str(e)}")

    if await GET_AFK():
        if message.chat.type == ChatType.PRIVATE or message.reply_to_message.from_user.id == OWNER_ID:
            try:
                afk_time = await GET_AFK_TIME()
                formatted_time = calculate_time(afk_time, datetime.now())
                reason = await GET_AFK_REASON()
                if reason is None:
                    await message.reply_text(f"**⚠️ OFFLINE WARNING ⚠️**\n\nSorry, My master is Currently Offline, You can't chat with my master currently now. and don't spam here because he/she may be in a highly stressed situation, working, or facing a problem. Please do not disturb him/her now.\n\n**➲ Reason: NOT SET\n➲ Offline Duration:** {formatted_time}")
                else:
                    await message.reply_text(f"**⚠️ OFFLINE WARNING ⚠️**\n\nSorry, My master is Currently Offline, You can't chat with my master currently now. and don't spam here because he/she may be in a highly stressed situation, working, or facing a problem. Please do not disturb him/her now.\n\n**➲ Reason: `{reason}`\n➲ Offline Duration:** {formatted_time}")
                    await Sophia.mark_chat_unread(message.chat.id)
            except Exception as e:
                print(e)
                await Sophia.send_message(OWNER_ID, f"Error in AFK handling: {str(e)}")
    return False

@Sophia.on_message(filters.create(filter_) & ~filters.bot & ~filters.service)
async def message_handle(_, message):
    # This function never triggered lol
    print("Join @Hyper_Speed0")
