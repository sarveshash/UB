from Restart import restart_program
from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.command("restart", prefixes=HANDLER) & filters.user(OWN))
async def Call_Restart_Func(_, message):
    await message.edit("`Killing all process`")
    await asyncio.sleep(0.34)
    await message.edit("`All process killed shuting down`")
    with open("others/restarted.py", "w") as mano:
        ctx = f"is_restarted = True\nrestart_msg = {message}"
        mano.write(ctx)
    restart_program()
