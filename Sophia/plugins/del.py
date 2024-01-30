from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters

@Sophia.on_message(filters.command(['del', 'delete'], prefixes=HANDLER) & filters.user(OWNER_ID))
async def message_del(_, message):
    if message.reply_to_message:
        try:
            await Sophia.delete_messages(message.chat.id, message.reply_to_message.message_id)
            await Sophia.delete_messages(message.chat.id, message.message_id)
        except Exception as e:
            await message.reply_text(f"Something went wrong. Please check errors:\n\n`{e}`")
    else:
        message_id = " ".join(message.command[1:])
        if message_id.isdigit():
            try:
                await Sophia.delete_messages(message.chat.id, int(message_id))
                await Sophia.delete_messages(message.chat.id, message.id)
            except Exception as e:
                await message.reply_text(f"Something went wrong. Please check errors:\n\n`{e}`")
        else:
            await message.reply_text("Please reply to a message or enter a valid message id.")
