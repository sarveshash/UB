from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from pyrogram import enums
from Sophia.Database.backup_msg import *

async def backup_enabled(_, client, update):
    if update.from_user.id == OWNER_ID:
        for x in HANDLER:
            if not len(update.text) < 2:
                if update.text.startswith(x) and update.from_user.id == OWNER_ID and await GET_BACKUP() and not update.chat.type == enums.ChatType.BOT:
                    return False
    if not await GET_BACKUP() and update.chat.id in await GET_STOP_BACKUP_CHATS():
        return False
    else:
        return True

@Sophia.on_message(filters.command(["chatbackup", "cbackup", "backup"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def enable_backup(_, message):
    STATUS = await GET_BACKUP()
    if not STATUS == True:
        await ENABLE_BACKUP()
        await message.reply("Ok bro")
    else:
        await DISABLE_BACKUP()
        await message.reply("Done bro")


@Sophia.on_message(filters.private & filters.create(backup_enabled) & ~filters.bot)
async def backup_chats(_, message):
    if not message.chat.id == OWNER_ID and message.chat.id in await GET_BACKUP_CHATS():
        chat_id = await GET_BACKUP_CHANNEL_ID(message.chat.id)
        try:
            if not message.chat.id == OWNER_ID and not message.chat.type == enums.ChatType.BOT:
                await Sophia.forward_messages(chat_id, message.chat.id, message.id)
                pass
        except Exception as e:
            if str(e) == """Telegram says: [400 CHANNEL_INVALID] - The channel parameter is invalid (caused by "channels.GetChannels")""":
                chat = await Sophia.create_channel(f"{message.chat.first_name} BACKUP", "~ @Hyper_Speed0")
                await ADD_BACKUP_CHAT(message.chat.id)
                await SET_BACKUP_CHANNEL_ID(message.chat.id, chat.id)
                await Sophia.forward_messages(chat.id, message.chat.id, message.id)
                await Sophia.archive_chats(chat.id)
                return
            else:
                print("Somthing went wrong in backup msg", e)
        pass
    else:
        if not message.chat.id == OWNER_ID and not message.chat.type == enums.ChatType.BOT:
            chat = await Sophia.create_channel(f"{message.chat.first_name} BACKUP", "~ @Hyper_Speed0")
            await ADD_BACKUP_CHAT(message.chat.id)
            await SET_BACKUP_CHANNEL_ID(message.chat.id, chat.id)
            await Sophia.forward_messages(chat.id, message.chat.id, message.id)
            await Sophia.archive_chats(chat.id)
        else:
            pass

@Sophia.on_message(filters.command(["resetbackup", "rbackup", "delbackup"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def delete_backup(_, message):
    if not message.chat.type == enums.ChatType.PRIVATE:
        return await message.reply("This command only works on Private chats")
    USERS = await GET_BACKUP_CHATS()
    if message.chat.id in USERS:
        CH = await GET_BACKUP_CHANNEL_ID(message.chat.id)
        try:
            await Sophia.delete_channel(CH)
            await message.reply("I have deleted this chat backup!")
        except Exception as e:
            if str(e) == """Telegram says: [400 CHANNEL_INVALID] - The channel parameter is invalid (caused by "channels.GetChannels")""" or str(e) == """Peer id invalid: 0""":
                return await message.reply("This chat backup channel was already deleted.")
            await message.reply(f"Error, {e}")
    else:
        await message.reply("This chat has no backup!")
        
@Sophia.on_message(filters.command("stopbackup", prefixes=HANDLER) & filters.user(OWNER_ID))
async def stop_backup(_, message):
    if not message.chat.type == enums.ChatType.PRIVATE:
        return await message.reply("This command Only works on Private chat")
    elif message.chat.id in await GET_STOP_BACKUP_CHATS():
        return await message.reply("This chat already stoped in backup")
    await ADD_STOP_BACKUP_CHAT(message.chat.id)
    await message.reply("I have stopped this chat from backup")

@Sophia.on_message(filters.command("unstopbackup", prefixes=HANDLER) & filters.user(OWNER_ID))
async def unstop_backup(_, message):
    if not message.chat.type == enums.ChatType.PRIVATE:
        return await message.reply("This command Only works on Private chat")
    elif message.chat.id not in await GET_STOP_BACKUP_CHATS():
        return await message.reply("This chat is not stoped in backup")
    await REMOVE_STOP_BACKUP_CHAT(message.chat.id)
    await message.reply("I have unstopped this chat from backup")
    
