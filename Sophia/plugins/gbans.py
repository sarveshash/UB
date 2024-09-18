from Sophia import HANDLER
from Sophia.__main__ import Sophia
from pyrogram import filters
import asyncio
import time
from pyrogram import enums

@Sophia.on_message(filters.command("gban", prefixes=HANDLER) & filters.me)
async def gban(_, message):
    me = await Sophia.get_me()
    me = me.id
    time_start = time.time()
    success_chats = 0
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == me:
            return await message.reply("You can't gban yourself!")
        loading_msg = await message.reply("Starting gban! ⚡")
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type in [enums.ChatType.SUPERGROUP, enums.ChatType.GROUP]:
                try:
                    await Sophia.ban_chat_member(dialog.chat.id, message.reply_to_message.from_user.id)
                    success_chats += 1
                    await asyncio.sleep(2)
                except Exception as e:
                    if not "CHAT_ADMIN_REQUIRED" in str(e) and not "FLOOD_WAIT_X" in str(e):
                        print(e)
        await loading_msg.delete()
        await message.reply(f"Gban completed in {success_chats} chats\nTaken time: {int(time.time() - time_start)}")
    else:
        if len(message.command) < 2:
            return await message.reply_text("Reply to a user or enter the user ID to gban")
        id = message.text.split(None, 1)[1]
        if not id.startswith(('@', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
            return await message.reply("Please enter a valid id.")
        id = int(id)
        if id == me:
            return await message.reply("You can't gban yourself!")
        loading_msg = await message.reply("Starting gban! ⚡")
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type in [enums.ChatType.SUPERGROUP, enums.ChatType.GROUP]:
                try:
                    await Sophia.ban_chat_member(dialog.chat.id, id)
                    success_chats += 1
                    await asyncio.sleep(2)
                except Exception as e:
                    if not "CHAT_ADMIN_REQUIRED" in str(e) and not "FLOOD_WAIT_X" in str(e):
                        print(e)
        await loading_msg.delete()
        await message.reply(f"Gban completed in {success_chats} chats\nTaken time: {int(time.time() - time_start)}")


@Sophia.on_message(filters.command("ungban", prefixes=HANDLER) & filters.me)
async def ungban(_, message):
    me = await Sophia.get_me()
    me = me.id
    time_start = time.time()
    success_chats = 0
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == me:
            return await message.reply("You can't ungban yourself!")
        loading_msg = await message.reply("Ungbaning....")
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type in [enums.ChatType.SUPERGROUP, enums.ChatType.GROUP]:
                try:
                    await Sophia.unban_chat_member(dialog.chat.id, message.reply_to_message.from_user.id)
                    success_chats += 1
                    await asyncio.sleep(2)
                except Exception as e:
                    if not "CHAT_ADMIN_REQUIRED" in str(e) and not "FLOOD_WAIT_X" in str(e):
                        print(e)
        await loading_msg.delete()
        await message.reply(f"Ungban completed in {success_chats} chats\nTaken time: {int(time.time() - time_start)}")
    else:
        if len(message.command) < 2:
            return await message.reply_text("Reply to a user or enter the user ID to ungban")
        id = message.text.split(None, 1)[1]
        if not id.startswith(('@', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
            return await message.reply("Please enter a valid id.")
        id = int(id)
        if id == me:
            return await message.reply("You can't ungban yourself!")
        loading_msg = await message.reply("Ungbaning....")
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type in [enums.ChatType.SUPERGROUP, enums.ChatType.GROUP]:
                try:
                    await Sophia.unban_chat_member(dialog.chat.id, id)
                    success_chats += 1
                    await asyncio.sleep(2)
                except Exception as e:
                    if not "CHAT_ADMIN_REQUIRED" in str(e) and not "FLOOD_WAIT_X" in str(e):
                        print(e)
        await loading_msg.delete()
        await message.reply(f"Ungban completed in {success_chats} chats\nTaken time: {int(time.time() - time_start)}")
