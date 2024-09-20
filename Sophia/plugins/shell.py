from Sophia.__main__ import Sophia
from pyrogram import filters
import asyncio
import io

user_shells = {}

async def run_command(shell, command):
    shell.stdin.write(f"{command}\n".encode())
    await shell.stdin.drain()
    output = await shell.stdout.readuntil(b'\n')
    return output.decode()

@Sophia.on_message(filters.command("sh", prefixes=HANDLER) & filters.user("me"))
async def start_shell(_, message):
    user_id = message.from_user.id
    if user_id not in user_shells:
        shell = await asyncio.create_subprocess_exec(
            "/bin/bash", "-i",
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        user_shells[user_id] = shell
    command = str(message.text.split(None, 1)[1])
    shell = user_shells[user_id]
    try:
        output = await run_command(shell, command)
    except Exception as e:
        print("Error:", e)
        return await message.reply_text(f"Error running command: {e}")
    if len(output) > 4096:
        with io.BytesIO(str.encode(output)) as out_file:
            out_file.name = "command_output.txt"
            await message.reply_document(out_file)
    else:
        await message.reply_text(f"Output:\n`{output}`")


@Sophia.on_message(filters.command("esh", prefixes=HANDLER)filters.user("me"))
async def exit_shell(_, message):
    user_id = message.from_user.id
    shell = user_shells.pop(user_id)
    shell.terminate()
    await message.reply_text("Live shell session closed.")
