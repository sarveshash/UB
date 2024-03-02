from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
from Sophia.Database.copy_msg import *
import asyncio
import os

@Sophia.on_message(filters.command("copy", prefixes=HANDLER) & filters.user(OWNER_ID))
async def Copy_msg(_, message):
    if not message.reply_to_message:
        return await message.reply("Reply to a message to copy it.")
    else:
        try:
            COPIED_MSG = message.reply_to_message.message_id
            COPIED_MSG_CHAT = message.chat.id
            STORE = await SAVE_MSG(COPIED_MSG, COPIED_MSG_CHAT)
            if STORE == "SUCCESS":
                await message.reply("Successfully copied!")
            else:
                await message.reply(f"Error: {STORE}")
        except Exception as e:
            return await message.reply(f"Error: {e}")

@Sophia.on_message(filters.command("paste", prefixes=HANDLER) & filters.user(OWNER_ID))
async def paste_msg(_, message):
    COPIED_MSG = await COPIED()
    if not COPIED_MSG == True:
        return await message.reply("Clipboard is empty.")
    else:
        await Sophia.copy_message(message.chat.id, await CHAT_ID(), await MSG_ID())

@Sophia.on_message(filters.command("ncpaste", prefixes=HANDLER) & filters.user(OWNER_ID))
async def no_caption_paste_msg(_, message):
    COPIED_MSG = await COPIED()
    if not COPIED_MSG == True:
        return await message.reply("Clipboard is empty.")
    else:
        await Sophia.copy_message(message.chat.id, await CHAT_ID(), await MSG_ID(), caption="")
