from Restart import restart_program
from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from config import Do_you_need_warnings
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.command("restart", prefixes=HANDLER) & filters.user(OWN))
async def Call_Restart_Func(_, message):
    Restart_Msg = await message.edit("`Restarting Sophia....`")
    if Do_you_need_warnings == True:
        await asyncio.sleep(0.4)
        await Restart_Msg.edit("**⚠️ Warning ⚠️** `This Will Restart All UserBot Process And You cannot cancel it now ❌`")
    else:
        await restart_program()
