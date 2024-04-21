from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import time
from pyrogram import enums

@Sophia.on_message(filters.command("madd", prefixes=HANDLER) & filters.user(OWNER_ID))
async def gban(_, message):
    time_start = time.time()
    success = 0
    if message.reply_to_message:
        loading_msg = await message.reply("Adding member...")
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type == enums.ChatType.SUPERGROUP or dialog.chat.type == enums.ChatType.GROUP:
                try:
                    chat = dialog.chat
                    await chat.add_members(message.reply_to_message.from_user.id)
                    success += 1
                    await asyncio.sleep(2)
                except Exception as e:
                    if not str(e) == """Telegram says: [400 CHAT_ADMIN_REQUIRED] - The method requires chat admin privileges (caused by "messages.UpdatePinnedMessage")""" and not str(e).startswith("Telegram says: [420 FLOOD_WAIT_X] - A wait"):
                        print(e)
        await loading_msg.delete()
        await message.reply(f"Successfully added in {success_chats} chats\nTaken time: {int(time.time() - time_start)}")
    else:
        await message.reply("Please reply to a user to mass adding")
