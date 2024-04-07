from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import time
from pyrogram import enums

@Sophia.on_message(filters.command("gban", prefixes=HANDLER) & filters.user(OWNER_ID))
async def gban(_, message):
    time_start = time.time()
    success_chats = 0
    if message.reply_to_message:
        loading_msg = await message.reply("Gbaning....")
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type == enums.ChatType.SUPERGROUP or dialog.chat.type == enums.ChatType.GROUP:
                try:
                    await Sophia.ban_chat_member(dialog.chat.id, message.reply_to_message.from_user.id)
                    success_chats += 1
                    await asyncio.sleep(2)
                except Exception as e:
                    if not str(e) == """Telegram says: [400 CHAT_ADMIN_REQUIRED] - The method requires chat admin privileges (caused by "messages.UpdatePinnedMessage")""" and not str(e).startswith("Telegram says: [420 FLOOD_WAIT_X] - A wait"):
                        print(e)
        await loading_msg.delete()
        await message.reply(f"Gban completed in {success_chats} chats\nTaken time: {int(time.time() - time_start)}")
    else:
        if len(message.command) < 2:
            return await message.reply_text("Reply a user or enter the user id to gban")
        loading_msg = await message.reply("Gbaning....")
        id = int(message.text.split(None, 1)[1])
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type == enums.ChatType.SUPERGROUP or dialog.chat.type == enums.ChatType.GROUP:
                try:
                    await Sophia.ban_chat_member(dialog.chat.id, id)
                    success_chats += 1
                    await asyncio.sleep(2)
                except Exception as e:
                    if not str(e) == """Telegram says: [400 CHAT_ADMIN_REQUIRED] - The method requires chat admin privileges (caused by "messages.UpdatePinnedMessage")""" and not str(e).startswith("Telegram says: [420 FLOOD_WAIT_X] - A wait"):
                        print(e)
        await loading_msg.delete()
        await message.reply(f"Gban completed in {success_chats} chats\nTaken time: {int(time.time() - time_start)}")
