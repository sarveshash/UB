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
    code = message.text.replace(message.text.split(" ")[0], "")
    message.edit("Pʀᴏᴄᴇssɪɴɢ...")
    output = run(code)
    message.edit(f"```shell\n{output}```")
