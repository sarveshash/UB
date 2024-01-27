from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os

is_busy = {}

@Sophia.on_message(filters.command(["busy", "afk", "offline"], prefixes=HANDLER) & filters.user(OWN))
async def set_busy(_, message):
    is_busy = True
    await message.reply("Master, You are Successfully Set in To Busy Mode.")

@Sophia.on_message()
async def Say_Offline(_, message):
    if is_busy == True:
        if message.from_user.id == OWN:
            is_busy = False
            return
        await message.reply("Sorry My Owner is Currently Offline come later.")
