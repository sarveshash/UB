import os
from pyrogram import filters
from telegraph import upload_file
from config import OWNER_ID
from Sophia.__main__ import Sophia
from Sophia import HANDLER

@Sophia.on_message(filters.command(["tgm", "tm"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("Reply to Video or Image")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Oops! File Not Supported bruh")
        return
    location1 = await client.download_media(
        message=message.reply_to_message,
        file_name="Sophia/downloads/",
    )
    try:
        response = upload_file(location1)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            f"**Your link Generated** 👉 `https://telegra.ph{response[0]}` ",
            disable_web_page_preview=True,
        )
    finally:
        os.remove(location1)
