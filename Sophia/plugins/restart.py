from Restart import restart_program
from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.command("restart", prefixes=HANDLER) & filters.user(OWN))
async def Call_Restart_Func(_, message):
    Restart_Msg = await message.edit("`Restarting Sophia...`")
    restart_program()
