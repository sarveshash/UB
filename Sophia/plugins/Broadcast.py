from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from pyrogram import enums

@Sophia.on_message(filters.command("broadcastall", prefixes=HANDLER) & filters.user(OWNER_ID))
async def broadcast_all(_, message):
    SUCCESS = 0
    FAILED = 0
    if message.reply_to_message:
        async for dialog in Sophia.get_dialogs():
            if not dialog.chat.type == enums.ChatType.CHANNEL and not dialog.chat.type == enums.ChatType.BOT:
                try:
                    await Sophia.forward_messages(dialog.chat.id, message.chat.id, message.reply_to_message_id)
                    SUCCESS += 1
                except Exception:
                    FAILED += 1
        await message.reply(f"**Broadcast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")
    else:
        if len(message.command) < 2:
            return await message.reply_text("➲ Master, Please enter a text to broadcast or reply a message to broadcast.")
        text = message.text.split(None, 1)[1]
        async for dialog in Sophia.get_dialogs():
            if not dialog.chat.type == enums.ChatType.CHANNEL and not dialog.chat.type == enums.ChatType.BOT:
                try:
                    await Sophia.send_message(dialog.chat.id, text)
                    SUCCESS += 1
                except Exception:
                    FAILED += 1
        await message.reply(f"**Broadcast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")

@Sophia.on_message(filters.command(["gcast", "groupcast"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def GroupCast(_, message):
    SUCCESS = 0
    FAILED = 0
    if message.reply_to_message:
        async for dialog in Sophia.get_dialogs():
            if not dialog.chat.type == enums.ChatType.CHANNEL and not dialog.chat.type == enums.ChatType.BOT and not dialog.chat.type == enums.ChatType.PRIVATE:
                try:
                    await Sophia.forward_messages(dialog.chat.id, message.chat.id, message.reply_to_message_id)
                    SUCCESS += 1
                except Exception:
                    FAILED += 1
        await message.reply(f"**Groupcast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")
    else:
        if len(message.command) < 2:
            return await message.reply_text("➲ Master, Please enter a text to Groupcasting or reply a message to Groupcasting.")
        text = message.text.split(None, 1)[1]
        async for dialog in Sophia.get_dialogs():
            if not dialog.chat.type == enums.ChatType.CHANNEL and not dialog.chat.type == enums.ChatType.BOT and not dialog.chat.type == enums.ChatType.PRIVATE:
                try:
                    await Sophia.send_message(dialog.chat.id, text)
                    SUCCESS += 1
                except Exception:
                    FAILED += 1
        await message.reply(f"**Groupcast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")

@Sophia.on_message(filters.command(["ucast", "usercast"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def UserCast(_, message):
    SUCCESS = 0
    FAILED = 0
    if message.reply_to_message:
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type == enums.ChatType.PRIVATE:
                try:
                    await Sophia.forward_messages(dialog.chat.id, message.chat.id, message.reply_to_message_id)
                    SUCCESS += 1
                except Exception:
                    FAILED += 1
        await message.reply(f"**Usercast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")
    else:
        if len(message.command) < 2:
            return await message.reply_text("➲ Master, Please enter a text to Usercasting or reply a message to Usercasting.")
        text = message.text.split(None, 1)[1]
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type == enums.ChatType.PRIVATE:
                try:
                    await Sophia.send_message(dialog.chat.id, text)
                    SUCCESS += 1
                except Exception:
                    FAILED += 1
        await message.reply(f"**Usercast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")

@Sophia.on_message(filters.command(["chcast", "ccast", "channelcast"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def Channelcast(_, message):
    SUCCESS = 0
    FAILED = 0
    if message.reply_to_message:
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type == enums.ChatType.CHANNEL:
                try:
                    await Sophia.forward_messages(dialog.chat.id, message.chat.id, message.reply_to_message_id)
                    SUCCESS += 1
                except Exception:
                    FAILED += 1
        await message.reply(f"**Channelcast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")
    else:
        if len(message.command) < 2:
            return await message.reply_text("➲ Master, Please enter a text to Channelcasting or reply a message to Channelcasting.")
        text = message.text.split(None, 1)[1]
        async for dialog in Sophia.get_dialogs():
            if dialog.chat.type == enums.ChatType.CHANNEL:
                try:
                    await Sophia.send_message(dialog.chat.id, text)
                    SUCCESS += 1
                except Exception:
                    FAILED += 1
        await message.reply(f"**Channelcast Complete**\n\nSUCCESS = {SUCCESS}\nFAILED = {FAILED}")
        
