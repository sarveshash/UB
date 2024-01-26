from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.command("pin", prefixes=HANDLER) & filters.user(OWN))
async def pin_message(_, message):
    if message.reply_to_message:
        try:
            await Sophia.pin_chat_message(message.chat.id, message.reply_to_message_id)
            await message.edit("success")
        except Exception as e:
            await message.edit(f"**Sorry Master Somthing Went Wrong 💔**\n\n`{e}`")
    else:
        await message.edit("**Master Please reply to message for pin it 💖**")
