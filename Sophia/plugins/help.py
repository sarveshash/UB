from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.command("help", prefixes=HANDLER) & filters.user(OWNER_ID))
async def help(_, message):
    await message.reply(f"ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı\n\n-» Cʟɪᴄᴋ [ʜᴇʀᴇ](http://telegra.ph/Sophia-Commands-01-30) ᴛᴏ ɢᴇᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ.\n-» **Join**: @Hyper_Speed0©")
# Warning We just take Reference of text from ZaidUserbot
# And we don't created that "ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı" its from zaiduserbot Others are reference only
# If zaid seeing this if have problem contact me t.me/Otazuki I will change it!.
