from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os

is_busy_ = {}

@Sophia.on_message(filters.command(["busy", "afk", "offline"], prefixes=HANDLER) & filters.user(OWN))
async def set_busy(_, message):
    global is_busy_
    is_busy_ = True
    await message.reply("Master, You are Successfully Set in To Busy Mode.")

@Sophia.on_message()
async def Say_Offline(_, message):
    global is_busy_
    if is_busy_ == True:
        if message.from_user.id == OWN:
            is_busy_ = False
            return
        await message.reply("Sorry My Owner is Currently Offline come later.")
