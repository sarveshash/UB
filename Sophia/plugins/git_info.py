from requests import get
from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.command("git", prefixes=HANDLER) & filters.user(OWNER_ID))
async def git(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Master, give me GitHub username")
    user = message.text.split(None, 1)[1]
    res = get(f"https://api.github.com/users/{user}").json()
    data = f"""
Nᴀᴍᴇ: {res['name']}
Usᴇʀɴᴀᴍᴇ: `{res['login']}`
Lɪɴᴋ: [{res['login']}]({res['html_url']})
Bɪᴏ: `{res['bio']}`
Cᴏᴍᴘᴀɴʏ: {res['company']}
Bʟᴏɢ: {res['blog']}
Lᴏᴄᴀᴛɪᴏɴ: {res['location']}
Pᴜʙɪʟɪᴄ Rᴇᴘᴏs: `{res['public_repos']}`
Fᴏʟʟᴏᴡᴇʀs: `{res['followers']}`
Fᴏʟʟᴏᴡɪɴɢ: `{res['following']}`
Aᴄᴄᴏᴜɴᴛ Cʀᴇᴀᴛᴇᴅ: `{res['created_at']}`
"""
    with open(f"{user}.jpg", "wb") as f:
        kek = get(res["avatar_url"]).content
        f.write(kek)

    await message.reply_photo(f"{user}.jpg", caption=data)
    os.remove(f"{user}.jpg")
