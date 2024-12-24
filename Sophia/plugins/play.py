from Sophia import HANDLER
from Sophia.__main__ import Sophia as bot
from Sophia import SophiaVC
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os
import requests
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
from pytgcalls.types import MediaStream

vcInfo = {}

@bot.on_message(filters.command(["play", "sp"], prefixes=HANDLER) & filters.user(OWN) & ~filters.private & ~filters.bot)
async def play(_, message):
    global vcInfo
    try:
        await SophiaVC.start()
    except:
        pass
    if len(message.text.split()) < 2:
        if message.reply_to_message and message.reply_to_message.audio:
            try:
                m = await message.reply("📥 Downloading...")
                file = message.reply_to_message.audio
                path = await message.reply_to_message.download()
                title = file.title or "Unknown Title"
                dur = file.duration or 0
                await m.delete()
                await message.reply_photo(
                    photo="https://i.imgur.com/KdPrxqN.jpeg",
                    caption=(
                        f"**✅ Started Streaming On VC.**\n\n"
                        f"**🥀 Title:** {title[:20] if len(title) > 20 else title}\n"
                        f"**🐬 Duration:** {dur // 60}:{dur % 60:02d} Mins\n"
                        f"**🦋 Stream Type:** Telegram audio\n"
                        f"**👾 By:** SophiaUB\n"
                        f"**⚕️ Join:** __@Hyper_Speed0 & @FutureCity005__"
                    )
                )
                vcInfo[message.chat.id] = {"title": title, "duration": dur}
                await SophiaVC.play(message.chat.id, MediaStream(path))
                await manage_playback(message.chat.id, title, dur)
            except Exception as e:
                await message.reply(f"Error: {e}")
            return
        else:
            return await message.reply("Provide a song name or link.")
    query = " ".join(message.command[1:])
    m = await message.reply("🔄 Searching....")
    if query.startswith(("www.youtube", "http://", "https://")):
        link = query
        with YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(link, download=False)
            title = info.get("title", "Unknown Title")
            thumbnail = info.get("thumbnail")
            duration = info.get("duration")
    else:
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            link = f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
        except:
            await m.edit("⚠️ No results were found.")
            return
    thumb_name = f"{title}.jpg"
    if thumbnail:
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
    await m.edit("📥 Downloading...")
    try:
        ydl_opts = {"format": "bestaudio[ext=m4a]"}
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            audio_file = ydl.prepare_filename(info_dict)
        secmul, dur, dur_arr = 1, 0, str(duration).split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        await m.delete()
        await message.reply_photo(
            photo=thumb_name,
            caption=(
                f"**✅ Started Streaming On VC.**\n\n"
                f"**🥀 Title:** {title[:20] if len(title) > 20 else title}\n"
                f"**🐬 Duration:** {dur // 60}:{dur % 60:02d} Mins\n"
                f"**🦋 Stream Type:** Audio\n"
                f"**👾 By:** SophiaUB\n"
                f"**⚕️ Join:** __@Hyper_Speed0 & @FutureCity005__"
            )
        )
        vcInfo[message.chat.id] = {"title": title, "duration": dur}
        await SophiaVC.play(message.chat.id, MediaStream(audio_file))
        await manage_playback(message.chat.id, title, dur)
    except Exception as e:
        await message.reply(f"Error: {e}")
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except:
        pass

async def manage_playback(chat_id, title, duration):
    await asyncio.sleep(duration + 5)
    if vcInfo.get(chat_id, {}).get("title") == title:
        try:
            await SophiaVC.leave_call(chat_id)
            vcInfo.pop(chat_id, None)
        except Exception:
            pass

@bot.on_message(filters.command("skip", prefixes=HANDLER) & filters.user(OWN) & ~filters.private & ~filters.bot)
async def skip(_, message):
    if vcInfo.get(message.chat.id):
        try:
            await SophiaVC.leave_call(message.chat.id)
            vcInfo.pop(chat_id, None)
        except Exception as e:
            await message.reply('Nothing streaming in vc ❌')
    else:
        await message.reply('Nothing streaming in vc ❌')