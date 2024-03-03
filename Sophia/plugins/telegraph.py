import os
from pyrogram import filters
from telegraph import upload_file
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Sophia.__main__ import Sophia
from Sophia import HANDLER

@Sophia.on_message(filters.command(["tgm", "tm"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def gen_telegraph(_, message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("Master, reply to a media!")
    if reply.media:
      try:
          i = await message.reply("`Generating Telegraph Link...`")
          path = await reply.download()
          fk = upload_file(path)
          for x in fk:
              url = "https://graph.org/" + x
          await i.edit(f'**Your Telegraph Link Is Generated** [🎉](`{url}`)', disable_web_page_preview=True)
          os.remove(path)
      except Exception as e:
          await i.edit(f"ERROR: **{e}**")
          
          
# This code all rights reserved to © "https://t.me/Kalakar_Sangram"
