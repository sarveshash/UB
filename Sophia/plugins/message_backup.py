from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from pyrogram import enums

AVAILABLE_USERS = []
STATUS = False

@Sophia.on_message(filters.command(["chatbackup", "cbackup", "backup"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def enable_backup(_, message):
    global AVAILABLE_USERS, STATUS
    if not STATUS == True:
        STATUS = True
        await message.reply("Ok bro")
    else:
        STATUS = False
        await message.reply("Done bro")
