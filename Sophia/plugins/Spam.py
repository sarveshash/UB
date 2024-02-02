from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from config import Do_you_need_warnings
from pyrogram import filters
import asyncio
import os
from Restart import restart_program as spam_killer

what_is_text = {}
is_spam_running = {}
spam_stop = False

@Sophia.on_message(filters.command("spam", prefixes=HANDLER) & filters.user(OWN))
async def spam(_, message):
    global is_spam_running, spam_stop, what_is_text
    if len(message.text.split()) <2:
          return await message.reply_text("Master, give a input to spam")
    text = message.text.split(None, 1)[1]
    what_is_text = text
    is_spam_running = True
    await message.reply("Spam Started ⚡")
    while spam_stop == False:
        try:
            await Sophia.send_message(message.chat.id, text)
            await asyncio.sleep(1) # For stop flood wait 
        except Exception as e:
            print(e)
            spam_stop == True
            is_spam_running = False
            return

@Sophia.on_message(filters.command(["stopspam", "sspam", "endspam"], prefixes=HANDLER) & filters.user(OWN))
async def spam_stoper(_, message):
    global is_spam_running, spam_stop
    if is_spam_running == True:
        spam_stop = True
        is_spam_running = False
        await asyncio.sleep(1)
        spam_stop = False
        await message.reply_text("I stopped That spam successfully ✅")
    else:
        await message.reply_text('No Spam Currently Running??')
    @Sophia.on_message(filters.command(["fsspam", "killspam"], prefixes=HANDLER) & filters.user(OWN))
    async def Kill_The_Spam(_, message):
        await message.reply_text("What, spam not stoped yet?, Spam stoping...")
        await asyncio.sleep(0.7)
        if Do_you_need_warnings == True:
            await message.reply_text("**Warning ⚠️**: Its Restart All UserBot Process")
        await spam_killer()
