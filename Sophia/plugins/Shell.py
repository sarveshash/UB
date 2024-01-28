from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from pyrogram import filters
from subprocess import getoutput as run
import asyncio
import os

@Sophia.on_message(filters.command(["sh", "shell", "bash"], prefixes=HANDLER) & filters.user(OWN))
def shell(_, message):
    if len(message.command) < 2:
        message.edit("Mᴀsᴛᴇʀ, Pʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴄᴏᴅᴇ ᴛᴏ ʀᴜɴ ɪᴛ. 🥀 ✨")
        return
    code = " ".join(message.command[1:])
    message_text = message.reply_text("Pʀᴏᴄᴇssɪɴɢ...")
    output = run(code)
    message_text.edit(f"Oᴜᴛᴘᴜᴛ:\n`{output}`")
