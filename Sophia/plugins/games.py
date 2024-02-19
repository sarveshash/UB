from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from Sophia.Database.Games import *

@Sophia.on_message(filters.command("send", prefixes=HANDLER) & filters.user(OWNER_ID))
async def send_coins(_, message):
    
