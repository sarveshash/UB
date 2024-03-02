from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os

COPIED_MSG = 0
COPIED_MSG_CHAT = 0
COPIED = False

@Sophia.on_message(filters.command("copy", prefixes=HANDLER) & filters.user(OWNER_ID))
async def Copy_msg(_, message):
    global COPIED_MSG, COPIED_MSG_CHAT, COPIED
    if not message.reply_to_message:
        return await message.reply("Reply a message to copy it.")
    else:
        try:
            COPIED_MSG = message.reply_to_message_id
            COPIED_MSG_CHAT = message.chat.id
            COPIED = True
            await message.reply("Successfully copied!")
        except Exception as e:
            return await message.reply("Error", e)

@Sophia.on_message(filters.command("paste", prefixes=HANDLER) & filters.user(OWNER_ID))
async def paste_msg(_, message):
    global COPIED_MSG, COPIED_MSG_CHAT, COPIED
    if not COPIED == True:
        return await message.reply("Clipboard is empty.")
    else:
        await Sophia.copy_message(message.chat.id, COPIED_MSG_CHAT, COPIED_MSG)
