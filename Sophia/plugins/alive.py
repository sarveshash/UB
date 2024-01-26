from Sophia import *
from Sophia.__main__ import Sophia
from pyrogram import *
import asyncio

@Sophia.on_message(filters.command(["alive", "start"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def Sophia_Alive(_, message):
    await message.edit("◖⁠⚆⁠ᴥ⁠⚆⁠◗ Loading...")
    await message.edit("Success")
