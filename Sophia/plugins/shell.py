from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from pyrogram import filters
from subprocess import Popen, PIPE
import asyncio
import os
import io

@Sophia.on_message(filters.command(["sh", "shell", "bash"], prefixes=HANDLER) & filters.user('me'))
async def shell(_, message):

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
        my_filter = filters.create(lambda _, __, message: 
                               message.chat.id == message.chat.id and 
                               message.from_user.id == "me")

        try:
            response = await asyncio.wait_for(Sophia.wait_for_message(my_filter), timeout=60)
            return response.text
        except asyncio.TimeoutError:
            return None

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
        
