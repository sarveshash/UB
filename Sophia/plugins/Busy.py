from pyrogram import filters
from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from Restart import restart_program
import os

Busy_stats = False

@Sophia.on_message(filters.command(["busy", "offline", "afk"], prefixes=HANDLER) & filters.user(OWN))
async def set_into_busy(_, message):
    global Busy_stats
    Busy_stats = True
    await message.reply_text("Master, I set you In Busy Mode!")

if Busy_stats == True:
    @Sophia.on_message(~filters.user(OWN))
    async def say_master_is_busy(_, message):
        await message.reply_text("Sorry My Master Is Currently Busy")

@Sophia.on_message(filters.user(OWN))
async def remove_busy_mode(_, message):
    global Busy_stats
    if Busy_stats == True:
        await message.reply_text("I have Removed Your Offline Mode")
        await restart_program()
