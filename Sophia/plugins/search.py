from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from googlesearch import search

@Sophia.on_message(filters.command("search", prefixes=HANDLER) & filters.user(OWNER_ID))
async def search(_, message):
    if len(message.text.split()) <2:
        return await message.reply("Master, enter a text to search it.")
    query = " ".join(message.command[1:])
    links = ""
    for j in search(query, num=10, stop=10, pause=2):
        links += f"{j}\n"
    await message.reply(f"**Results:**:\n{h}", disable_web_page_preview=True)
