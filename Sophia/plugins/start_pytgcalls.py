from pyrogram import filters
from pytgcalls import idle
from Sophia import *

started = False

@Sophia.on_message(filters.command('pytg', prefixes=HANDLER) & filters.user('me'))
async def start_pytgcalls(_, message):
    global started
    if started:
        return await message.reply("Already pytgcalls client running!")
    mano = await message.reply("`Starting pytgcalls client...`")
    try:
        await Friday.start()
        await mano.edit("Successfuly started pytgcalls!")
        started = True
        await idle()
    except Exception as e:
        started = False
        await mano.edit(f"Error: {e}")
        print(f"Somthing went wrong while starting PyTgcalls: {e}")
