from gtts import gTTS
from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.command("tts", prefixes=HANDLER) & filters.user(OWNER_ID))
async def tts(_, message):
    m = message
    if not message.reply_to_message:
        return await m.reply("Please reply to a message!")
    elif len(message.command) < 2:
        return await m.reply(f"Please enter the language [code](https://graph.org/Language-codes-03-26)!", disable_web_page_preview=True)
    else:
        load = await m.reply('`Loading...`')
        try:
            text = message.reply_to_message.text
            if text == None:
                text = message.reply_to_message.caption
            language = " ".join(message.command[1:])
            language = language.lower()
            tts = gTTS(text=text, lang=language, slow=True)
            tts.save("output.oga")
            await m.reply_voice("output.oga")
        except ValueError:
            await m.reply(f"Please enter a correct language [code](https://graph.org/Language-codes-03-26)!", disable_web_page_preview=True)
        except Exception as e:
            await m.reply(f"Error: {e}")
            raise Exception(f"Error in TTS: {e}")
        await load.delete()
