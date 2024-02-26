from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from pyrogram import enums
from Sophia.Database.backup_msg import *

async def backup_enabled(_, client, update):
    if not await GET_BACKUP():
        return False
    else:
        return True

@Sophia.on_message(filters.command(["chatbackup", "cbackup", "backup"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def enable_backup(_, message):
    STATUS = await GET_BACKUP()
    if not STATUS == True:
        await ENABLE_BACKUP()
        await message.reply("Ok bro")
    else:
        await DISABLE_BACKUP()
        await message.reply("Done bro")


@Sophia.on_message(filters.private & filters.create(denied_users) & filters.incoming & ~filters.service & ~filters.me & ~filters.bot)
async def backup_chats(_, message):
    if message.chat.id in await GET_BACKUP_CHATS():
        print("Hi")
    else:
        chat = await Sophia.create_channel(f"{message.chat.id} BACKUP", "~ @Hyper_Speed0")
        await ADD_BACKUP_CHAT(message.chat.id)
        await SET_BACKUP_CHANNEL_ID(message.chat.id, chat.id)
