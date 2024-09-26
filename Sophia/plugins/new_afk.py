from Sophia import *
from pyrogram import *
from Sophia.Database.afk import *
from Sophia.Database.ignore_users import *
from Sophia.Database.backup_msg import *
from Sophia.Database.pmguard import *
from pyrogram.enums import *
from config import OWNER_ID
import os
import re
import asyncio

async def filter_(_, client, update):
    if await GET_BACKUP(): # Backup section
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
                    await Sophia.forward_messages(chat_id, message.chat.id, message.id)
                except:
                    if message.chat.username:
                        chat = await Sophia.create_channel(f"{message.chat.first_name} BACKUP", f"Username: @{message.chat.username}\n\n~ @Hyper_Speed0")
                    else:
                        chat = await Sophia.create_channel(f"{message.chat.first_name} BACKUP", "~ @Hyper_Speed0")
                    await ADD_BACKUP_CHAT(message.chat.id)
                    await SET_BACKUP_CHANNEL_ID(message.chat.id, chat.id)
                    await Sophia.forward_messages(chat.id, message.chat.id, message.id)
                    await Sophia.archive_chats(chat.id)
            else:
                
            
