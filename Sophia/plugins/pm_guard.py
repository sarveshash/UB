from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os

is_pm_block_enabled = False
approved_users = []
users_warngings_count = {}


@Sophia.on_message(filters.command("pmblock", prefixes=HANDLER) & filters.user(OWNER_ID))
async def set_pm_guard(_, message):
    global is_pm_block_enabled
    if is_pm_block_enabled:
        is_pm_block_enabled = False
    else:
        await message.reply('Feature coming soon')
        return
        

# Incompleted
