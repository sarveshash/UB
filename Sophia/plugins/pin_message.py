from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.command("pin", prefixes=HANDLER) & filters.user(OWN))
async def pin_message(_, message):
    await message.reply("under development")
