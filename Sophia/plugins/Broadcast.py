from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from Sophia.Database.Broadcast import *

@Sophia.on_message(filters.command("broadcastall", prefixes=HANDLER) & filters.user(OWNER_ID))
async def broadcast_all(_, message):
    LIST_CHATS = await GET_ALL_CHATS()
    for CHAT_ID in LIST_CHATS:
        await Sophia.send_message(CHAT_ID, "#TESTING BROADCAST\n - Powered by @Hyper_Speed0")
