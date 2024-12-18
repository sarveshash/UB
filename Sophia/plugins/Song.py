from Sophia import HANDLER
from Sophia.__main__ import Sophia as bot
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os
import requests
import wget
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
import yt_dlp


flex = {}
chat_watcher_group = 3

ydl_opts = {
    "format": "best",
    "keepvideo": True,
    "prefer_ffmpeg": False,
    "geo_bypass": True,
    "outtmpl": "%(title)s.%(ext)s",
    "quite": True,
}


@bot.on_message(filters.command("song", prefixes=HANDLER) & filters.user(OWN))
async def song(_, message):
    if len(message.text.split()) <2:
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
        await m.edit("📤 Uploading...")

        await message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            caption=f"{title}",
            duration=dur,
        )
        await m.delete()
    except Exception as e:
        await m.edit(f"**Error:**{e} ")
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

# Video


@bot.on_message(filters.command("video", prefixes=HANDLER) & filters.user(OWN))
async def video(client, message):
    if len(message.text.split()) <2:
        return await message.reply("Give a video name to search it")
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("Video Processing..")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 Error: {e}")
    preview = wget.download(thumbnail)
    await msg.edit("Process Complete.\n Now Uploading.")
    title = ytdl_data["title"]
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=f"**{title} Powered by: @Hyper_Speed0**",
    )

    await msg.delete()
    try:
        os.remove(file_name)
    except Exception as e:
        print(e)
