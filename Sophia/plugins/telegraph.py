import os
import logging
from pyrogram import filters
from telegraph import Telegraph
from config import OWNER_ID
from Sophia.__main__ import Sophia
from Sophia import HANDLER
from sobprocess import getoutput as r

# Initialize Telegraph only once
telegraph = Telegraph()
telegraph.create_account(short_name='my_bot')

@Sophia.on_message(filters.command(["tgm", "tm"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def telegraph_upload(client, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply("Reply to a video or image.")

    # Check if the replied media is supported
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
            and replied.document.file_name.endswith((".jpg", ".jpeg", ".png", ".gif", ".mp4"))
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Oops! File not supported or too large (max 5MB).")
        return

    try:
        location1 = await Sophia.download_media(
            message=message.reply_to_message,
            file_name="SophiaClient/downloads/"
        )

        if not location1 or not os.path.exists(location1):
            await message.reply("Error: File could not be downloaded.")
            return

        try:
            try:
                file_name_ = await r("ls SophiaClient/downloads/")
                pathhh = f"SophiaClient/downloads/{file_name_}"
                with open(pathhh, 'rb') as f:
                    response = telegraph.upload_file(f)
            except Exception as e:
                return await message.reply(f"Error on uploading file: {e}")

            # Check if response is a string (URL) or a dictionary
            if isinstance(response, str):
                # If it's a string, assume it's the URL
                src = response
                await message.reply(
                    f"**Your link has been generated**: 👉 `https://telegra.ph/{src}`",
                    disable_web_page_preview=True
                )
            elif isinstance(response, dict) and 'src' in response:
                # If it's a dictionary, extract the URL from 'src'
                src = response['src']
                await message.reply(
                    f"**Your link has been generated**: 👉 `https://telegra.ph/{src}`",
                    disable_web_page_preview=True
                )
            else:
                await message.reply("Error: Unexpected response from Telegraph upload.")

        except Exception as e:
            await message.reply(f"Error during upload: {str(e)}")

    finally:
        if location1 and os.path.exists(location1):
            os.remove(location1)
