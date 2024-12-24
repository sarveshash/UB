from Sophia import HANDLER
from Sophia.__main__ import Sophia
from pyrogram import filters
import asyncio
import os
from pyrogram import enums

@Sophia.on_message(filters.command(["bcast", "cast", "broadcast", "broadcastall"], prefixes=HANDLER) & filters.me)
async def broadcast_all(_, message):
    SUCCESS = 0
    FAILED = 0
    if message.reply_to_message:
        async for dialog in Sophia.get_dialogs():
            if not dialog.chat.type == enums.ChatType.CHANNEL and not dialog.chat.type == enums.ChatType.BOT:
                try:
                    msg = await Sophia.forward_messages(dialog.chat.id, message.chat.id, message.reply_to_message_id)
                    SUCCESS += 1
                    await asyncio.sleep(0.5)
                    await Sophia.pin_chat_message(dialog.chat.id, msg.id, disable_notification=True, both_sides=True)
                    await asyncio.sleep(2) # Controlling Account ban
                except Exception as e:
                    if not str(e) == """Telegram says: [400 CHAT_ADMIN_REQUIRED] - The method requires chat admin privileges (caused by "messages.UpdatePinnedMessage")""" and not str(e).startswith("Telegram says: [420 FLOOD_WAIT_X] - A wait"):
                        FAILED += 1
        await message.reply(f"**Broadcast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")
    else:
        if len(message.command) < 2:
            return await message.reply_text("➲ Master, Please enter a text to broadcast or reply a message to broadcast.")
        text = message.text.split(None, 1)[1]
        async for dialog in Sophia.get_dialogs():
            if not dialog.chat.type == enums.ChatType.CHANNEL and not dialog.chat.type == enums.ChatType.BOT:
                try:
                    msg = await Sophia.send_message(dialog.chat.id, text)
                    SUCCESS += 1
                    await asyncio.sleep(0.5)
                    await Sophia.pin_chat_message(dialog.chat.id, msg.id, disable_notification=True, both_sides=True)
                    await asyncio.sleep(2)
                except Exception as e:
                    if not str(e) == """Telegram says: [400 CHAT_ADMIN_REQUIRED] - The method requires chat admin privileges (caused by "messages.UpdatePinnedMessage")""" and not str(e).startswith("Telegram says: [420 FLOOD_WAIT_X] - A wait"):
                        FAILED += 1
        await message.reply(f"**Broadcast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")

@Sophia.on_message(filters.command(["gcast", "groupcast"], prefixes=HANDLER) & filters.me)
async def GroupCast(_, message):
    SUCCESS = 0
    FAILED = 0
    if message.reply_to_message:
        async for dialog in Sophia.get_dialogs():
            if not dialog.chat.type == enums.ChatType.CHANNEL and not dialog.chat.type == enums.ChatType.BOT and not dialog.chat.type == enums.ChatType.PRIVATE:
                try:
                    msg = await Sophia.forward_messages(dialog.chat.id, message.chat.id, message.reply_to_message_id)
                    SUCCESS += 1
                    await asyncio.sleep(0.5)
                    await Sophia.pin_chat_message(dialog.chat.id, msg.id, disable_notification=True, both_sides=True)
                    await asyncio.sleep(2)
                except Exception as e:
                    if not str(e) == """Telegram says: [400 CHAT_ADMIN_REQUIRED] - The method requires chat admin privileges (caused by "messages.UpdatePinnedMessage")""" and not str(e).startswith("Telegram says: [420 FLOOD_WAIT_X] - A wait"):
                        FAILED += 1
        await message.reply(f"**Groupcast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")
    else:
        if len(message.command) < 2:
            return await message.reply_text("➲ Master, Please enter a text to Groupcasting or reply a message to Groupcasting.")
        text = message.text.split(None, 1)[1]
        async for dialog in Sophia.get_dialogs():
            if not dialog.chat.type == enums.ChatType.CHANNEL and not dialog.chat.type == enums.ChatType.BOT and not dialog.chat.type == enums.ChatType.PRIVATE:
                try:
                    msg = await Sophia.send_message(dialog.chat.id, text)
                    SUCCESS += 1
                    await asyncio.sleep(0.5)
                    await Sophia.pin_chat_message(dialog.chat.id, msg.id, disable_notification=True, both_sides=True)
                    await asyncio.sleep(2)
                except Exception as e:
                    if not str(e) == """Telegram says: [400 CHAT_ADMIN_REQUIRED] - The method requires chat admin privileges (caused by "messages.UpdatePinnedMessage")""" and not str(e).startswith("Telegram says: [420 FLOOD_WAIT_X] - A wait"):
                        FAILED += 1
        await message.reply(f"**Groupcast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")

@Sophia.on_message(filters.command(["ucast", "usercast"], prefixes=HANDLER) & filters.me)
async def UserCast(_, message):
    SUCCESS = 0
    FAILED = 0
    if message.reply_to_message:
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type == enums.ChatType.PRIVATE:
                try:
                    msg = await Sophia.forward_messages(dialog.chat.id, message.chat.id, message.reply_to_message_id)
                    SUCCESS += 1
                    await asyncio.sleep(2)
                except Exception as e:
                    FAILED += 1
        await message.reply(f"**Usercast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")
    else:
        if len(message.command) < 2:
            return await message.reply_text("➲ Master, Please enter a text to Usercasting or reply a message to Usercasting.")
        text = message.text.split(None, 1)[1]
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type == enums.ChatType.PRIVATE:
                try:
                    msg = await Sophia.send_message(dialog.chat.id, text)
                    SUCCESS += 1
                    await asyncio.sleep(2)
                except Exception as e:
                    FAILED += 1
        await message.reply(f"**Usercast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")

@Sophia.on_message(filters.command(["chcast", "ccast", "channelcast"], prefixes=HANDLER) & filters.me)
async def Channelcast(_, message):
    SUCCESS = 0
    FAILED = 0
    if message.reply_to_message:
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type == enums.ChatType.CHANNEL:
                try:
                    await Sophia.forward_messages(dialog.chat.id, message.chat.id, message.reply_to_message_id)
                    SUCCESS += 1
                    await asyncio.sleep(2)
                except Exception as e:
                    FAILED += 1
        await message.reply(f"**Channelcast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")
    else:
        if len(message.command) < 2:
            return await message.reply_text("➲ Master, Please enter a text to Channelcasting or reply a message to Channelcasting.")
        text = message.text.split(None, 1)[1]
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type == enums.ChatType.CHANNEL:
                try:
                    msg = await Sophia.send_message(dialog.chat.id, text)
                    SUCCESS += 1
                    await asyncio.sleep(2)
                except Exception as e:
                    FAILED += 1
        await message.reply(f"**Channelcast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")
