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
        await message.reply("Reply to a video or image.")
        return

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

    # Download the media to a local file
    location1 = await client.download_media(
        message=message.reply_to_message,
        file_name="Sophia/downloads/"
    )

    # Check if the file was downloaded successfully
    if not location1 or not os.path.exists(location1):
        await message.reply("Error: File could not be downloaded.")
        return

    try:
        # Upload the file to Telegraph
        response = upload_file(location1)
    except Exception as e:
        await message.reply(f"Error during upload: {str(e)}")
        return
    else:
        # Reply with the generated link
        await message.reply(
            f"**Your link has been generated**: 👉 `https://telegra.ph{response[0]}`",
            disable_web_page_preview=True
        )
    finally:
        # Clean up by removing the downloaded file
        os.remove(location1)
