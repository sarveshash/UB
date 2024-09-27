from pyrogram.enums import ChatType
from pyrogram import *
from Sophia import *
from config import OWNER_ID

@Sophia.on_message(filters.command("delchat", HANDLER) & filters.user('me'))
async def delete_chat(_, m):
  if not message.chat.type == ChatType.PRIVATE:
    return await m.reply("Please use this command on private chat!")
  if message.chat.id == OWNER_ID:
    return await m.reply("Sorry you cannot use this here!")
  try:
    await Sophia.delete_chat_history(m.chat.id)
    await m.reply("Successfuly deleted the chat!")
  except Exception as e:
    print(f"Something went wrong while deleting chat on {m.chat.id}: {e}")
