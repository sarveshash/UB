from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from config import SUDO_USERS_ID as loyal
from pyrogram import filters
from subprocess import Popen, PIPE
import asyncio
import os
import io

@Sophia.on_message(filters.command(["sh", "shell", "bash"], prefixes=HANDLER) & ~filters.bot)
async def shell(_, message):
    if message.from_user.id == OWN or message.from_user.id in loyal:
        print("")
    else:
        return

    process = None

    async def process_output(process, message_text):
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                try:
                    await message_text.edit(f"Oᴜᴛᴘᴜᴛ:\n`{output.strip()}`")
                except:
                    pass

    async def get_input():
        response = await Sophia.listen(filters.chat(message.chat.id) & filters.user("me"))
        return response.text

    if len(message.command) < 2:
        await message.edit("Mᴀsᴛᴇʀ, Pʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴄᴏᴅᴇ ᴛᴏ ʀᴜɴ ɪᴛ. 🥀 ✨")
        return
    code = message.text.split(None, 1)[1]
    message_text = await message.reply_text("Pʀᴏᴄᴇssɪɴɢ...")

    process = Popen(code, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True, bufsize=1)

    asyncio.create_task(process_output(process, message_text))

    while process.poll() is None:
        user_input = await get_input()
        if user_input:
            process.stdin.write(user_input + '\n')
            process.stdin.flush()
    output, error = process.communicate()
    if error:
        await message_text.edit(f"Error:\n`{error}`")
    else:
        await message_text.edit(f"Oᴜᴛᴘᴜᴛ:\n`{output.strip()}`")
