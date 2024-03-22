from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from Sophia.Database.ignore_bad import *
from pyrogram import filters
import asyncio
import re

async def bad_word_remover_stats(_, client, update):
    ignore_bad = IGNORE_BAD()
    is_enabled = await ignore_bad.GET()
    if is_enabled and update.chat.id != OWNER_ID:
        return True
    else:
        return False

bad_words = [
    'punda', 'fuck', 'ommala'
]

pattern = r"\b(?:{})\b".format('|'.join(['{}(?:{})?'.format(re.escape(word), '[a-zA-Z]*' * (len(word)-1)) for word in bad_words]))

@Sophia.on_message(filters.text & filters.regex(pattern, re.IGNORECASE) & filters.create(bad_word_remover_stats))
async def remove_message(_, message):
    try:
        await message.delete()
    except Exception as e:
        if str(e) == """Telegram says: [403 MESSAGE_DELETE_FORBIDDEN] - You don't have rights to delete messages in this chat, most likely because you are not the author of them (caused by "channels.DeleteMessages")""":
            return
        print(e)
        await Sophia.send_message(message.chat.id, f"Error: {e}")

@Sophia.on_message(filters.command(["ignorebad", "stopbad"], prefixes=HANDLER) & filters.me)
async def set_ignore_bad(_, message):
    try:
        ignore_bad = IGNORE_BAD()
        log = await ignore_bad.ENABLE()
        if log == "SUCCESS":
            await message.reply("Let's ignore bad things!")
        else:
            await message.reply(f"Error: {log}")
            print(log)
    except Exception as e:
        await message.reply(f"Error: {e}")
        print(e)
        
