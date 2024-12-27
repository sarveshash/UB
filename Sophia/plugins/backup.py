from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import re
import os
from pyrogram import enums
from Sophia.Database.ignore_bad import *
from Restart import restart_program as restart
from Sophia.Database.backup_msg import *
from Sophia.plugins.ignore_bad import pattern



@Sophia.on_message(filters.command("backup", prefixes=HANDLER) & filters.user(OWNER_ID))
async def enable_backup(_, message):
    STATUS = await GET_BACKUP()
    if not STATUS == True:
        await ENABLE_BACKUP()
        await message.reply("Successfully enabled backup mode!")
    else:
        await DISABLE_BACKUP()
        await message.reply("Successfully disabled backup mode!")

                


@Sophia.on_message(filters.command(["resetbackup", "rbackup", "delbackup"], prefixes=HANDLER) & filters.user(OWNER_ID) & filters.private)
async def delete_backup(_, message):
    USERS = await GET_BACKUP_CHATS()
    if message.chat.id in USERS:
        CH = await GET_BACKUP_CHANNEL_ID(message.chat.id)
        try:
            await SET_BACKUP_CHANNEL_ID(message.chat.id, 0)
            eee = await message.reply("I have deleted this chat backup!")
            await Sophia.delete_channel(CH)
            await message.reply("I have deleted this chat backup!")
        except Exception as e:
            if str(e) == """Telegram says: [400 CHANNEL_INVALID] - The channel parameter is invalid (caused by "channels.GetChannels")""" or str(e) == """Peer id invalid: 0""":
                return await eee.edit("This chat backup channel was already deleted.")
            await message.reply(f"Error, {e}")
    else:
        await message.reply("This chat has no backup!")
        
@Sophia.on_message(filters.command(["stopbackup", "sbackup"], prefixes=HANDLER) & filters.user(OWNER_ID) & filters.private)
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

@Sophia.on_message(filters.command(["unstopbackup", "usbackup"], prefixes=HANDLER) & filters.user(OWNER_ID) & filters.private)
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

MOD_NAME = 'Backup'
MOD_HELP = """.backup - Use in pm/db to save the messages in a private channel.
.sbackup - Stop backup-ing for temporary 
.usbackup - To unstop the backup-ing.
.rbackup - To delete/reset the backup (the channel will deleted)

**💡Pro tip:** Simply use this command for scammer/your friend """
