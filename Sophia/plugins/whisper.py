from Sophia import HANDLER, SophiaBot, Sophia, qfilter
from pyrogram import *
import logging
from pyrogram.types import *
from config import OWNER_ID
import json
from pyrogram import enums
import traceback 
from Sophia.Database.whisper import whisper

whs = whisper()

@Sophia.on_message(filters.command("whisper", prefixes=HANDLER) & filters.user(OWNER_ID) & ~filters.private & ~filters.bot)
async def whisper(_, message):
    await message.delete()
    if len(message.text.split()) < 2:
        return await message.reply("Please enter a text to whisper!")
    if not message.reply_to_message:
        return await message.reply("Please reply to someone to whisper!")
    reply = message.reply_to_message
    data = {
        'name': f"{reply.from_user.first_name} {reply.from_user.last_name or ''}".strip(),
        'id': reply.from_user.id,
        'message': " ".join(message.command[1:]),
        'username': reply.from_user.username or 'Nothing'
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

@SophiaBot.on_inline_query(qfilter("whisper: "))
async def send_whisper(_, query):
    try:
        data = json.loads(query.query.replace("whisper: ", ""))
        wid = await whs.add(data['message'], data['id'])
        mention = f"https://t.me/{data['username']}" if data.get('username') != 'Nothing' else ' '
        button = InlineKeyboardMarkup([[InlineKeyboardButton("View 🔓", callback_data=f"wh: {wid}")]])
        result = InlineQueryResultArticle(
            title="Whisper message",
            input_message_content=InputTextMessageContent(
                f"""🔒 A whisper message to [{data['name']}]({mention}), only they can open it.

                {f"**🦋 To: @{data['username']}" if data['username'] != "Nothing" else ""}
                **👾 By:** SophiaUB
                """,
                parse_mode=enums.ParseMode.MARKDOWN,
                disable_web_page_preview=True
            ),
            reply_markup=button
        )
        await query.answer([result])
    except:
        e = traceback.format_exc()
        logging.error(e)

@SophiaBot.on_callback_query(qfilter("wh: "))
async def show_whisper(_, query):
    try:
        wid = int(query.data.replace("wh: ", ""))
        data = await whs.get(wid)
        if data and (query.from_user.id == data['id'] or query.from_user.id == OWNER_ID):
            await query.answer(data['message'], show_alert=True)
        else:
            await query.answer("This message is not for you.", show_alert=False)
    except:
        e = traceback.format_exc()
        logging.error(e)

MOD_NAME = "Whisper"
MOD_HELP = ".whisper <text & reply> - To send a message privately like @WhisperBot!"
