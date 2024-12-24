# LOL MODULE, I don't know why i created this 😂

from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters

@Sophia.on_message(filters.command("say", prefixes=HANDLER) & filters.user(OWNER_ID))
async def say(_, m):
  message=m
  try:
    await m.delete()
  except:
    pass 
  if m.reply_to_message:
    if not m.reply_to_message.media_group_id:
      return await Sophia.copy_message(m.chat.id, m.chat.id, m.reply_to_message.id)
    return await Sophia.copy_media_group(m.chat.id, m.chat.id, m.reply_to_message.id)
  else:
    if len(m.command) >= 2:
      txt = m.text.split(None, 1)[1]
      await Sophia.send_message(m.chat.id, )
