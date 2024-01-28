from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os

Busy_stats = False

@Sophia.on_message(filters.command(["busy", "offline", "afk"], prefixes=HANDLER) & filters.user(OWN))
async def Set_into_busy(_, message):
    global Busy_stats
    Busy_stats = True
    await message.reply_text("Master, I set you In Busy Mode!")

@Sophia.on_message(~filters.user(OWN))
async def Say_master_is_busy(_, message):
    global Busy_stats
    if Busy_stats == True:
        await message.reply_text("Sorry My Master Is Current Busy")
if Busy_stats == True:
    @Sophia.on_message(filters.user(OWN))
    async def Remove_busy_Mode(_, message):
        global Busy_stats
        Busy_stats = False
        await message.reply_text("I have Removed Your Offline Mode")
