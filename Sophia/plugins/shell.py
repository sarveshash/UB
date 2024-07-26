from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from config import SUDO_USERS_ID as loyal
from pyrogram import filters
from subprocess import getoutput as run
import asyncio
import os
import io

@Sophia.on_message(filters.command(["sh", "shell", "bash"], prefixes=HANDLER) & ~filters.bot)
async def shell(_, message):
    if message.from_user.id == OWN or message.from_user.id in loyal:
        print("")
    else:
        return
    if len(message.command) < 2:
        await message.edit("Mᴀsᴛᴇʀ, Pʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴄᴏᴅᴇ ᴛᴏ ʀᴜɴ ɪᴛ. 🥀 ✨")
        return
    code = message.text.split(None, 1)[1]
    message_text = await message.reply_text("Pʀᴏᴄᴇssɪɴɢ...")
    output = await run(code)
    if len(output) > 4096:
        with io.BytesIO(str.encode(output)) as out_file:
            out_file.name = "shell.txt"
            await message.reply_document(
                document=out_file, disable_notification=True
            )
            await message_text.delete()
    else:
        await message_text.edit(f"Oᴜᴛᴘᴜᴛ:\n`{output}`")
    
