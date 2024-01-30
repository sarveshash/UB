from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from config import SUDO_USERS_ID as loyal
from pyrogram import filters
from subprocess import getoutput as run
import asyncio
import os

@Sophia.on_message(filters.command(["sh", "shell", "bash"], prefixes=HANDLER))
def shell(_, message):
    if message.from_user.id == OWN or message.from_user.id in loyal:
        print("")
    else:
        return
    if len(message.command) < 2:
        message.edit("Mᴀsᴛᴇʀ, Pʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴄᴏᴅᴇ ᴛᴏ ʀᴜɴ ɪᴛ. 🥀 ✨")
        return
    code = message.text.split(None, 1)[1]
    message_text = message.reply_text("Pʀᴏᴄᴇssɪɴɢ...")
    output = run(code)
    message_text.edit(f"Oᴜᴛᴘᴜᴛ:\n`{output}`")
