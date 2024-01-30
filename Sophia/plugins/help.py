from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.command("help", prefixes=HANDLER) & filters.user(OWNER_ID))
async def help(_, message):
    await message.reply(f"ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı\n\n-» Cʟɪᴄᴋ [ʜᴇʀᴇ](http://telegra.ph/Sophia-Commands-01-30) ᴛᴏ ɢᴇᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ.\n-» **Join**: @Hyper_Speed0©")
