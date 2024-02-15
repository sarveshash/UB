from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from pyrogram import enums

@Sophia.on_message(filters.command("block", prefixes=HANDLER) & filters.user(OWNER_ID))
async def block_user(_, message):
    if message.chat.type == enums.ChatType.PRIVATE:
        try:
            await Sophia.block_user(message.chat.id)
            await message.reply("➲ I successfully blocked this user ✅.")
        except Exception as e:
            await message.reply("ERROR", e)
    else:
        await message.reply("➲ This command Only works on Private Chat.")
        return


@Sophia.on_message(filters.command("unblock", prefixes=HANDLER) & filters.user(OWNER_ID))
async def unblock_user(_, message):
    if message.chat.type == enums.ChatType.PRIVATE:
        try:
            await Sophia.unblock_user(message.chat.id)
            await message.reply("➲ I successfully unblocked this user ✅.")
        except Exception as e:
            await message.reply("ERROR", e)
    else:
        await message.reply("➲ This command Only works on Private Chat.")
        return
        
            
