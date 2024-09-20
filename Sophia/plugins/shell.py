from Sophia import HANDLER
from Sophia.__main__ import Sophia
from pyrogram import filters
from subprocess import getoutput as run
import asyncio
import os
import io

@Sophia.on_message(filters.command(["sh", "shell", "bash"], prefixes=HANDLER) & filters.user('me'))
async def shell(_, message):
    if len(message.command) < 2:
        return await message.edit("Please enter a command to run! 🥀 ✨")
    code = message.text.split(None, 1)[1]
    message_text = await message.reply_text("`Processing...`")
    output = run(code)
    if len(output) > 4096:
        with io.BytesIO(str.encode(output)) as out_file:
            out_file.name = "shell.txt"
            await message.reply_document(
                document=out_file, disable_notification=True
            )
            await message_text.delete()
    else:
        await message_text.edit(f"**Output**:\n`{output}`")
