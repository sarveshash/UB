from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
from pyrogram import enums
from pyrogram import enums
from Restart import restart_program as restart
from Sophia.Database.backup_msg import *

async def backup_enabled(_, client, update):
    message = update
    if update.from_user.id == OWNER_ID:
        for x in HANDLER:
            if update.text:
                if update.text.startswith(x) and await GET_BACKUP() and not len(update.text) < 2:
                    return False
    if not await GET_BACKUP():
        return False
    else:
        if update.chat.id in await GET_STOP_BACKUP_CHATS():
            return False
        return True

async def group_backup(_, client, update):
    if not await GET_BACKUP(group=True):
        return False
    else:
        if update.chat.id in await GET_STOP_BACKUP_CHATS():
            return False
        return True

@Sophia.on_message(filters.command(["chatbackup", "cbackup", "backup"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def enable_backup(_, message):
    STATUS = await GET_BACKUP()
    if not STATUS == True:
        await ENABLE_BACKUP()
        await message.reply("Successfully enabled backup mode!")
    else:
        await DISABLE_BACKUP()
        await message.reply("Successfully disabled backup mode!")

@Sophia.on_message(filters.command("gbackup", prefixes=HANDLER) & filters.user(OWNER_ID))
async def enable_group_backup(_, message):
    STATUS = await GET_BACKUP(group=True)
    if not STATUS == True:
        await ENABLE_BACKUP(group=True)
        await message.reply("Successfully enabled group backup mode!")
    else:
        await DISABLE_BACKUP(group=True)
        await message.reply("Successfully disabled group backup mode!")
        


@Sophia.on_message(filters.private & filters.create(backup_enabled) & ~filters.bot)
async def backup_chats(_, message):
    if not message.chat.id == OWNER_ID and message.chat.id in await GET_BACKUP_CHATS():
        chat_id = await GET_BACKUP_CHANNEL_ID(message.chat.id)
        try:
            await Sophia.forward_messages(chat_id, message.chat.id, message.id)
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

@Sophia.on_message(filters.group & filters.create(group_backup) & ~filters.bot & ~filters.text)
async def backup_group_chats(_, message):
    CHATS = await GET_BACKUP_CHATS()
    if message.chat.id in CHATS:
        chat_id = await GET_BACKUP_CHANNEL_ID(message.chat.id)
        try:
            await Sophia.forward_messages(chat_id, message.chat.id, message.id)
        except Exception as e:
            if str(e) == """Telegram says: [400 CHANNEL_INVALID] - The channel parameter is invalid (caused by "channels.GetChannels")""":
                chat = await Sophia.create_channel(f"{message.chat.title} GROUP BACKUP", "~ @Hyper_Speed0")
                await ADD_BACKUP_CHAT(message.chat.id)
                await SET_BACKUP_CHANNEL_ID(message.chat.id, chat.id)
                await Sophia.forward_messages(chat.id, message.chat.id, message.id)
                return await Sophia.archive_chats(chat.id)
            else:
                print("Somthing went wrong in backup msg", e)
    else:
        chat = await Sophia.create_channel(f"{message.chat.title} GROUP BACKUP", "~ @Hyper_Speed0")
        await ADD_BACKUP_CHAT(message.chat.id)
        await SET_BACKUP_CHANNEL_ID(message.chat.id, chat.id)
        await Sophia.forward_messages(chat.id, message.chat.id, message.id)
        await Sophia.archive_chats(chat.id)
                


@Sophia.on_message(filters.command(["resetbackup", "rbackup", "delbackup"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def delete_backup(_, message):
    USERS = await GET_BACKUP_CHATS()
    if message.chat.id in USERS:
        CH = await GET_BACKUP_CHANNEL_ID(message.chat.id)
        try:
            await Sophia.delete_channel(CH)
            await message.reply("I have deleted this chat backup!")
            await restart()
        except Exception as e:
            if str(e) == """Telegram says: [400 CHANNEL_INVALID] - The channel parameter is invalid (caused by "channels.GetChannels")""" or str(e) == """Peer id invalid: 0""":
                return await message.reply("This chat backup channel was already deleted.")
            await message.reply(f"Error, {e}")
    else:
        await message.reply("This chat has no backup!")
        
@Sophia.on_message(filters.command(["stopbackup", "sbackup"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def stop_backup(_, message):
    if message.chat.id in await GET_STOP_BACKUP_CHATS():
        return await message.reply("This chat already stoped in backup")
    await ADD_STOP_BACKUP_CHAT(message.chat.id)
    try:
        CH = await GET_BACKUP_CHANNEL_ID(message.chat.id)
        await Sophia.send_message(CH, "**BACKUP STOPED**")
    except Exception:
        n = 0
    await message.reply("I have stopped this chat from backup")

@Sophia.on_message(filters.command(["unstopbackup", "usbackup"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def unstop_backup(_, message):
    if message.chat.id not in await GET_STOP_BACKUP_CHATS():
        return await message.reply("This chat is not stoped in backup")
    await REMOVE_STOP_BACKUP_CHAT(message.chat.id)
    try:
        CH = await GET_BACKUP_CHANNEL_ID(message.chat.id)
        await Sophia.send_message(CH, "**BACKUP UNSTOPED**")
    except Exception:
        n = 0
    await message.reply("I have unstopped this chat from backup")
    
@Sophia.on_message(filters.command("schats", prefixes=HANDLER) & filters.user(OWNER_ID))
async def get_stoped_backup_chats(_, message):
    MSG = await message.reply("`Processing...`")
    NAMES = []
    FORMATTED_NAMES = ""
    async for dialog in Sophia.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            if dialog.chat.id in await GET_STOP_BACKUP_CHATS():
                GET_CHAT = await Sophia.get_chat(dialog.chat.id)
                First_name = GET_CHAT.first_name
                NAMES.append(First_name)
    for name in NAMES:
        FORMATTED_NAMES += f"-» `{name}`\n"
    await MSG.edit(f"**Results:**\n{FORMATTED_NAMES}")
