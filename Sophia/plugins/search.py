from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from googlesearch import search

@Sophia.on_message(filters.command("search", prefixes=HANDLER) & filters.user(OWNER_ID))
async def search(_, message):
    if len(message.text.split()) < 2:
        return await message.reply("Master, enter a text to search it.")
    MSG = await message.reply("`Loading...`")
    query = " ".join(message.command[1:])
    links = ""
    for j in search(query, stop=10, pause=2):
        links += f"{j}\n"
    await MSG.edit(f"**Results:**:\n\n{links}", disable_web_page_preview=True)
