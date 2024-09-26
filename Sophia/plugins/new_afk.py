from Sophia import *
from pyrogram import *
from Sophia.Database.afk import *
from Sophia.Database.ignore_users import *
from Sophia.Database.backup_msg import *
from Sophia.Database.pmguard import *
from pyrogram.enums import *
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
        if not command and update.chat.id not in await GET_STOP_BACKUP_CHATS():
            
            
