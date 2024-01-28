from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os

is_spam_running = {}
spam_stop = False

@Sophia.on_message(filters.command("spam", prefixes=HANDLER) & filters.user(OWN))
async def spam(_, message):
    global is_spam_running, spam_stop
    if len(message.text.split()) <2:
          return await message.reply_text("Master, give a input to spam")
    if spam_stop == True:
        spam_stop == False
    text = message.text.split(None, 1)[1]
    is_spam_running = True
    await message.reply("Spam Started ⚡")
    while spam_stop == False:
        await Sophia.send_message(message.chat.id, text)

@Sophia.on_message(filters.command(["stopspam", "sspam", "endspam"], prefixes=HANDLER) & filters.user(OWN))
async def spam_stoper(_, message):
    global is_spam_running, spam_stop
    if is_spam_running == False:
        spam_stop = True
        is_spam_running = False
        await message.reply_text("I stopped That spam successfully ✅")
    else:
        await message.reply_text('No Spam Currently Running??')
