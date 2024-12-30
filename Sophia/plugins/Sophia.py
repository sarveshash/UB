from Sophia import HANDLER
from Sophia import *
from config import OWNER_ID
from pyrogram import filters
import asyncio
from pyrogram import enums
import os
from pyrogram import *
import asyncio
from pyrogram.types import InlineQueryResultPhoto, InlineKeyboardMarkup, InlineKeyboardButton

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
