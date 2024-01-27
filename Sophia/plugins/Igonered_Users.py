from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID, IGNORED_USERS_ID
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.command(filters.user(IGNORED_USERS_ID))
async def Ignored_chat(_, message):
    Name = Sophia.get_me()
    await message.reply_text("I ᴀᴍ ɴᴏᴛ {}, ɪ'ᴍ Sᴏᴘʜɪᴀ ᴀ Vɪʀᴜᴛᴀʟ ||Assistant||. Fᴏʀ {},\n ʜᴇ/sʜᴇ Iɢɴᴏʀᴇᴅ ʏᴏᴜ sᴏ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴄʜᴀᴛ ᴡɪᴛʜ ʜɪᴍ/ʜᴇʀ")
