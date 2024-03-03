import io
import sys
import traceback
from Sophia import *
from config import SUDO_USERS_ID
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from pyrogram import enums
from Sophia.Database.games import *

app = Sophia
Client = Sophia
bot = Sophia

@Sophia.on_message(filters.command(["eval", "e", "python"], prefixes=HANDLER))
async def eval(client, message):
    if not message.from_user.id == OWNER_ID or message.from_user.id not in SUDO_USERS_ID:
        return
    if len(message.command) < 2:
        return await message.reply_text("Master, Please Enter code to run it!. ✨ 🥀")
    status_message = await message.reply_text("`Processing...`")
    cmd = message.text.split(None, 1)[1]

    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "INPUT: "
    final_output += f"{cmd}\n\n"
    final_output += "OUTPUT:\n"
    final_output += f"{evaluation.strip()} \n"
    output_code = f"""```python\n{evaluation.strip()}```"""

    if len(output_code) >= 3500:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.txt"
            await reply_to_.reply_document(
                document=out_file, caption=cmd, disable_notification=True
            )
    else:
        await reply_to_.reply_text(output_code)
    await status_message.delete()


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)
