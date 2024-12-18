from Sophia import HANDLER
from Sophia.__main__ import Sophia as bot
from Sophia import SophiaVC
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os
import requests
import logging
import wget
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
import yt_dlp
from pytgcalls import *
from pytgcalls.types import MediaStream


flex = {}
chat_watcher_group = 3

ydl_opts = {
    "format": "low",
    "keepvideo": True,
    "prefer_ffmpeg": False,
    "geo_bypass": True,
    "outtmpl": "%(title)s.%(ext)s",
    "quite": True,
}


@bot.on_message(filters.command(["play", "sp"], prefixes=HANDLER) & filters.user(OWN))
async def play(_, message):
    try:
        await SophiaVC.start()
    except:
        None
    if len(message.text.split()) <2:
        if message.reply_to_message and message.reply_to_message.audio:
            try:
                m = await message.reply("📥 Downloading...")
                audio = message.reply_to_message.audio
                audioPath = await message.reply_to_message.download()
                title = message.reply_to_message.audio.title
                dur = message.reply_to_message.audio.duration
                await m.delete()
                await message.reply_photo(
                    photo="https://i.imgur.com/KdPrxqN.jpeg",
                    caption=(
                        f"**✅ Started Streaming On VC.**\n\n"
                        f"**🥀 Title:** {title[:19] if len(title) > 19 else title}\n"
                        f"**🐬 Duration:** {dur // 60}:{dur % 60:02d} Mins\n"
                        f"**🦋 Stream Type:** Telegram Audio\n"
                        f"**👾 By:** SophiaUB\n"
                        f"**⚕️ Join:** __@Hyper_Speed0 & @FutureCity005__"
                    )
                )
                await SophiaVC.play(message.chat.id, MediaStream(audioPath))
                try:
                    await asyncio.sleep(dur)
                    await SophiaVC.leave_call(message.chat.id)
                except:
                    None
                return
            except Exception as e:
                await message.reply(f"Error: {e}")
                logging.error(e)
                return
        else:
            return await message.reply("Give a song name to search it")
    query = " ".join(message.command[1:])
    m = await message.reply("🔄 Searching....")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:4000]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        await m.edit(
            "⚠️ No results were found. Make sure you typed the information correctly"
        )
        print(str(e))
        return
    await m.edit("📥 Downloading...")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        await m.delete()
        await message.reply_photo(
            photo=thumb_name,
            caption=(
                f"**✅ Started Streaming On VC.**\n\n"
                f"**🥀 Title:** {title[:19] if len(title) > 19 else title}\n"
                f"**🐬 Duration:** {dur // 60}:{dur % 60:02d} Mins\n"
                f"**🦋 Stream Type:** Audio\n"
                f"**👾 By:** SophiaUB\n"
                f"**⚕️ Join:** __@Hyper_Speed0 & @FutureCity005__"
            )
        )
        await SophiaVC.play(message.chat.id, MediaStream(audio_file))
        try:
            await asyncio.sleep(dur)
            await SophiaVC.leave_call(message.chat.id)
        except:
            None
        
    except Exception as e:
        await message.reply(f"Error: {e} ")
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
