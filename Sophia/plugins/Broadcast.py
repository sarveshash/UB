from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from Sophia.Database.Broadcast import *

@Sophia.on_message(filters.command("broadcastall", prefixes=HANDLER) & filters.user(OWNER_ID))
async def broadcast_all(_, message):
    # Ntg
