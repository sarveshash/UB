from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.command("pin", prefixes=HANDLER) & filters.user(OWN))
async def pin_message(_, message):
    if message.reply_to_message:
        try:
            await Sophia.pin_chat_message(message.chat.id, message.reply_to_message_id)
            await message.edit("Dᴏɴᴇ ✅")
        except Exception as e:
            if str(e) == """Telegram says: [400 CHAT_ADMIN_REQUIRED] - The method requires chat admin privileges (caused by "messages.UpdatePinnedMessage")""":
                await message.edit("Mᴀsᴛᴇʀ, ᴡᴇ ɴᴇᴇᴅ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ᴛᴏ ᴅᴏ ᴛʜɪs ❌")
                return
            await message.edit(f"**Sᴏʀʀʏ, ᴍᴀsᴛᴇʀ sᴏᴍᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ ᴘʟᴇᴀsᴇ ᴄʜᴇᴀᴄᴋ ᴇʀʀᴏʀs 💔**\n\n`{e}`")
    else:
        await message.edit("**Mᴀsᴛᴇʀ, Pʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ғᴏʀ ᴘɪɴɴɪɴɢ ɪᴛ ❤️**")


@Sophia.on_message(filters.command("unpin", prefixes=HANDLER) & filters.user(OWN))
async def pin_message(_, message):
    if message.reply_to_message:
        try:
            await Sophia.unpin_chat_message(message.chat.id, message.reply_to_message_id)
            await message.edit("Dᴏɴᴇ ✅")
        except Exception as e:
            if str(e) == """Telegram says: [400 CHAT_ADMIN_REQUIRED] - The method requires chat admin privileges (caused by "messages.UpdatePinnedMessage")""":
                await message.edit("Mᴀsᴛᴇʀ, ᴡᴇ ɴᴇᴇᴅ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ᴛᴏ ᴅᴏ ᴛʜɪs ❌")
                return
            await message.edit(f"**Sᴏʀʀʏ, ᴍᴀsᴛᴇʀ sᴏᴍᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ ᴘʟᴇᴀsᴇ ᴄʜᴇᴀᴄᴋ ᴇʀʀᴏʀs 💔**\n\n`{e}`")
    else:
        await message.edit("**Mᴀsᴛᴇʀ, Pʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ғᴏʀ ᴜɴᴘɪɴɴɪɴɢ ɪᴛ ❤️**")
        
