from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os

Number = ["1","2","3","4","5","6","7","8","9","0"]
@Sophia.on_message(filters.command(['del', 'delete'], prefixes=HANDLER) & filters.user(OWNER_ID))
async def message_del(_, message):
    if message.reply_to_message:
        try:
            await Sophia.delete_messages(message.chat.id, message.reply_to_message_id)
            await Sophia.delete_messages(message.chat.id, message.id)
        except Exception as e:
            await message.reply_text(f"Somthing went wrong please check errors:\n\n`{e}`")
    else:
        message_id = " ".join(message.command[1:])
        if message_id.startswith(Number):
            try:
                await Sophia.delete_messages(message.chat.id, message_id)
                await Sophia.delete_messages(message.chat.id, message.id)
            except Exception as e:
                await message.reply_text(f"Somthing went wrong please check errors:\n\n`{e}`")
        else:
            await message.reply_text("Please reply to a message or enter message id!.")
