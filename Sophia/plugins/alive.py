from Sophia import HANDLER, OWNER_ID
from Sophia.__main__ import Sophia
from pyrogram import *
import asyncio

@Sophia.on_message(filters.command("alive", prefixes=HANDLER) & filters.user(OWNER_ID))
async def Sophia_Alive(_, message):
    await message.edit("◖⁠⚆⁠ᴥ⁠⚆⁠◗ Loading...")
    await asyncio.sleep(1.2)
    await message.edit("Success")
