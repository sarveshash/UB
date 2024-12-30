from Sophia import HANDLER
from Sophia import *
from config import OWNER_ID
from pyrogram import filters
import asyncio
import logging
from pyrogram import enums
import os
from datetime import datetime
from pyrogram import *
import asyncio
import traceback
from Sophia.plugins.modules import a, help_names
from Sophia.plugins.ping import ping_website
from pyrogram.types import *
from pyrogram import __version__
from Sophia.plugins.play import vcInfo


@SophiaBot.on_inline_query(filters.regex('IRLYMANOFR'))
async def send_btns(_, query):
  try:
    btns = InlineKeyboardMarkup([
      [
        InlineKeyboardButton("🆕 What is new?", callback_data=f"SophiaNew"),
        InlineKeyboardButton("⚙️ Settings", callback_data=f"SophiaPageSettigns")
      ],
      [
        InlineKeyboardButton("🗂️ GitHub", url=f"https://github.com/Otazuki004/SophiaUB"),
        InlineKeyboardButton("📖 Help", callback_data=f"helppage:1")
      ],
      [
        InlineKeyboardButton("⚕️ Stats ⚕️", callback_data=f"SophiaStats")
      ],
      [
        InlineKeyboardButton("👥 Community", url="https://t.me/Hyper_Speed0")
      ]
    ])
    result = InlineQueryResultPhoto(
      photo_url="https://i.imgur.com/lgzEDVh.jpeg",
      caption="Sophia system..",
      reply_markup=btns
    )
    await query.answer([result])
  except:
    e = traceback.format_exc()
    logging.error(e)

@SophiaBot.on_callback_query(filters.regex('SophiaStats'))
async def show_stats(_, query):
  start_time = bot_start_time
  end_time = datetime.now()
  ping_time = (end_time - start_time).total_seconds() * 1000
  uptime = (end_time - bot_start_time).total_seconds()
  hours, remainder = divmod(uptime, 3600)
  minutes, seconds = divmod(remainder, 60)
  stats_txt = f"""𝗦𝗼𝗽𝗵𝗶𝗮 𝗦𝘆𝘀𝘁𝗲𝗺\n
Uᴘᴛɪᴍᴇ: {int(hours)}h {int(minutes)}m {int(seconds)}s
Pʏᴛʜᴏɴ: {python_version}
Pʏʀᴏɢʀᴀᴍ: {__version__}
Pɪɴɢ: {ping_website("https://google.com")}
Sᴏɴɢs ᴘʟᴀʏɪɴɢ: {len(vcInfo) if vcInfo else 0}
Hᴇʟᴘ ᴍᴏᴅᴜʟᴇs: {len(help_names)}/{len(a)}
Mʏ ᴠᴇʀsɪᴏɴ: {MY_VERSION}
Rᴇʟᴇᴀsᴇ ᴛʏᴘᴇ: {release_type}
  """
  await query.answer(stats_txt, show_alert=True)

@SophiaBot.on_callback_query(filters.regex('SophiaNew'))
async def show_newUpdates(_, query):
  await query.answer(what_is_new, show_alert=True)

@SophiaBot.on_callback_query(filters.regex('SophiaPageSettigns'))
async def show_settings(_, query):
  if query.from_user.id != OWNER_ID:
        return await query.answer('This is not for you!', show_alert=False)
  await query.answer("Coming soon", show_alert=False)

@Sophia.on_message(filters.command(["sophia", "stats"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def send_stats(_, message):
    results = await Sophia.get_inline_bot_results(SophiaBot.me.username, 'IRLYMANOFR')
    await Sophia.send_inline_bot_result(
        chat_id=message.chat.id,
        query_id=results.query_id,
        result_id=results.results[0].id
    )

@SophiaBot.on_inline_query(filters.regex('SophiaReportBug'))
async def send_reportBug(_, query):
  try:
    btn = InlineKeyboardMarkup([[InlineKeyboardButton("🪲 Report a bug", user_id=5965055071)]])
    result = InlineQueryResultArticle(
      title="Report bug",
      input_message_content=InputTextMessageContent(
        f"Click the button below to report bug 🪲"
      ),
      reply_markup=btn
    )
    await query.answer([result])
  except:
    e = traceback.format_exc()
    logging.error(e)

@Sophia.on_message(filters.command("bug", prefixes=HANDLER) & filters.user(OWNER_ID))
async def send_rbug(_, message):
    results = await Sophia.get_inline_bot_results(SophiaBot.me.username, 'SophiaReportBug')
    await Sophia.send_inline_bot_result(
        chat_id=message.chat.id,
        query_id=results.query_id,
        result_id=results.results[0].id
    )
  
