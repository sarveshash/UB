from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
from pyrogram import enums
import os

@Sophia.on_message(filters.command("stats", prefixes=HANDLER) & filters.user(OWNER_ID))
async def stats(_, message):
    m = message
    msg = await m.reply("Analysing...")
    groups, users, channels = 0, 0, 0
    async for dialog in Sophia.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            users += 1
        elif dialog.chat.type == enums.ChatType.CHANNEL:
            channels += 1
        elif dialog.chat.type == enums.ChatType.GROUP or dialog.chat.type == enums.ChatType.SUPERGROUP:
            groups += 1
    await msg.edit(f"Stats\nusers={users}\nchannels={channels}\ngroups={groups}")
        
            
