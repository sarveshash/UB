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
        await message.reply("I disabled Pmblock")
    else:
        is_pm_block_enabled = True
        await message.reply('done ✅')
        return
        
@Sophia.on_message(~filters.user(OWNER_ID))
async def warn_users(_, message):
    if message.from_user.id in approved_users:
        return
    if is_pm_block_enabled:
        await message.reply("I am warning you lol just ub test baka")
