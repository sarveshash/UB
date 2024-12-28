from Sophia import HANDLER, SophiaBot, Sophia, qfilter
from pyrogram import *
import logging
from pyrogram.types import *
from config import OWNER_ID
import json
from Sophia import *
from Sophia.Database.whisper import *

whs = whisper()

@Sophia.on_message(filters.command("whisper", prefixes=HANDLER) & filters.user(OWNER_ID) & ~filters.private & ~filters.bot)
async def whisper(_, message):
    await message.delete()
    if len(message.text.split()) < 2:
        return await message.reply("Please enter a text to whisper!")
    if not message.reply_to_message:
        return await message.reply('Please reply someone to whisper!')
    reply = message.reply_to_message
    data = {
        'name': str(reply.from_user.first_name),
        'id': reply.from_user.id,
        'message': str(" ".join(message.command[1:]))
    }
    results = await Sophia.get_inline_bot_results(SophiaBot.me.username, f"whisper: {json.dumps(data)}")
    if results.results:
        await Sophia.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=results.query_id,
            result_id=results.results[0].id
        )
    else:
        await message.reply("Error: No result returned by the inline bot.")

@SophiaBot.on_inline_query(qfilter('whisper: '))
async def send_whisper(_, query):
    try:
        data = json.loads(str(query.query).replace('whisper: ', ''))
        wid = await whs.add(data['message'], data['id'])
        button = InlineKeyboardMarkup([[InlineKeyboardButton("View 🔓", callback_data=f"wh: {wid}")]])
        result = InlineQueryResultArticle(
            title="Whisper message",
            input_message_content=InputTextMessageContent(
                f"🔒 A whisper message to {data['name']}, Only he/she can open it."
            ),
            reply_markup=button
        )
        await query.answer([result])
    except Exception as e:
        logging.error(e)

@SophiaBot.on_callback_query(qfilter('wh: '))
async def show_whisper(_, query):
    try:
        wid = int(query.data.replace('wh: ', ''))
        data = await whs.get(wid)
        if data and query.from_user.id == data['id'] or query.from_user.id == OWNER_ID:
            await query.answer(data['message'], show_alert=True)
        else:
            await query.answer("This message not for you.", show_alert=False)
    except Exception as e:
        logging.error(e)

MOD_NAME = 'Whisper'
MOD_HELP = "Beta module help updated soon!"
