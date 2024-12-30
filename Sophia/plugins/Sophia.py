from Sophia import HANDLER
from Sophia import *
from config import OWNER_ID
from pyrogram import filters
import asyncio
from pyrogram import enums
import os
from pyrogram import *
import asyncio
from Sophia.plugins.modules import a, help_names
from Sophia.plugins.ping import ping_website
from pyrogram.types import InlineQueryResultPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import __version__

@SophiaBot.on_inline_query(filters.regex('IRLYMANOFR'))
async def send_btns(_, query):
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
  Pɪɴɢ: {ping_website("https://google.com")}ms
  Sᴏɴɢs ᴘʟᴀʏɪɴɢ: 0
  Hᴇʟᴘ Mᴏᴅᴜʟᴇs: {len(help_names)}/{len(a)}
  Mʏ ᴠᴇʀsɪᴏɴ: {MY_VERSION}
  """
  await query.answer(stats_txt, show_alert=True)
