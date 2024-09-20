from Sophia import HANDLER
from Sophia import Sophia
from pyrogram import filters
from subprocess import getoutput as run
import asyncio
import os
import io

run("apt update && apt install -y nodejs npm && nvm install node && curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash")

@Sophia.on_message(filters.command(["js", "jse"], prefixes=HANDLER) & filters.user('me'))
async def run_js(_, message):
    if len(message.command) < 2:
        return await message.edit("Please enter a JavaScript command to run! 🥀 ✨")
    js_code = message.text.split(None, 1)[1]
    message_text = await message.reply_text("Processing...")
    js_code = js_code.replace('${', '`').replace('}', '`')
    with open("MyProgram.js", "w") as js_file:
        js_file.write(js_code)
    output = run("node MyProgram.js")
    os.remove("MyProgram.js")
    if len(output) > 4096:
        with io.BytesIO(str.encode(output)) as out_file:
            out_file.name = "js_output.txt"
            await message.reply_document(
                document=out_file, disable_notification=True
            )
            await message_text.delete()
    else:
        await message_text.edit(f"Output:\n```Output\n{output}```")
