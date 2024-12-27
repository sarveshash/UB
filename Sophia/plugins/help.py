from Sophia import HANDLER
from Sophia.__main__ import Sophia, SophiaBot
from config import OWNER_ID
from config import SUDO_USERS_ID
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.command("help", prefixes=HANDLER) & filters.user(OWNER_ID))
async def help(_, message):
    results = await Sophia.get_inline_bot_results(SophiaBot.me.username, 'help')
    await Sophia.send_inline_bot_result(
        chat_id=message.chat.id,
        query_id=results.query_id,
        result_id=results.results[0].id
    )
    
