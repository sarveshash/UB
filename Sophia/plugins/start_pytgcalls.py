from pyrogram import filters
from pytgcalls import idle
from Sophia import *

started = False

@Sophia.on_message(filters.command('pytg', prefixes=HANDLER) & filters.user('me'))
async def start_pytgcalls(_, message):
    global started
    if started:
        return await message.reply("Already pytgcalls client running!")
    await message.reply("Successfuly started pytgcalls client!")
    started = True
    idle()
