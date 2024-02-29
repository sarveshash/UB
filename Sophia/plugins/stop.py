from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from Restart import restart_program as restart

@Sophia.on_message(filters.command("stop", prefixes=HANDLER) & filters.user(OWNER_ID))
async def stop_ub(_, message):
    await message.reply("I have stopped for 5sec")
    Sophia.stop()
    await asyncio.sleep(5)
    await restart()
    
