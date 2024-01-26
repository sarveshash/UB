from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.command("alive", prefixes=HANDLER) & filters.user(OWN))
async def Sophia_Alive(_, message):
    await message.edit("◖⁠⚆⁠ᴥ⁠⚆⁠◗ Loading...")
    await asyncio.sleep(1.2)
    await message.edit("Success")
