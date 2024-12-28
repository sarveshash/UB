from Sophia import HANDLER
from Sophia.__main__ import Sophia as bot
from Sophia import SophiaVC
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os
import re
import requests
import traceback
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
from pytgcalls.types import MediaStream
from Sophia.Database.play import *

vcInfo = {}
PLAYPREFIXES = HANDLER
PLAYPREFIXES += ["/"]
oh = play()
Sophia = bot
async def publicFilter(_, client, message):
    if not message.text.startswith(tuple(PLAYPREFIXES)): return False
    if message.from_user.id == OWN: return True
    if message.chat.id in await oh.get() and message.text.startswith(("/", ".", "$")): return True
    return False

@bot.on_message(filters.command(["addplay", 'aplay'], prefixes=HANDLER) & filters.user(OWN) & ~filters.private & ~filters.bot)
async def addPlayGroups(_, message):
    chat_id = message.chat.id
    info = await oh.addRemove(chat_id)
    if info == "SUCCESS": await message.reply('Successfully allowed play commands in this chat ✅')
    elif info == 'ALREADY': await message.reply("❌ This chat already have permission to use play commands!")

@bot.on_message(filters.command("rplay", prefixes=HANDLER) & filters.user(OWN) & ~filters.private & ~filters.bot)
async def removePlayGroups(_, message):
    chat_id = message.chat.id
    info = await oh.addRemove(chat_id, addOrRemove='remove')
    if info == "SUCCESS": await message.reply('Successfully removed play commands access in this chat ✅')
    elif info == 'ALREADY': await message.reply("❌ This chat already don't have permission to use play commands!")

@bot.on_message(filters.command("getplay", prefixes=HANDLER) & filters.user(OWN) & ~filters.private & ~filters.bot)
async def getPlayGroups(_, message):
    info = await oh.get()
    a = await message.reply("Searching...")
    txt = ""
    for x in info:
        try:
            d = await Sophia.get_chat(x)
            txt += f"{d.title}{'' if not d.username else f' | @{d.username}'}\n"
        except Exception as e:
            logging.error(e)
            pass
    await a.delete()
    if info and txt: return await message.reply(f"**⚕️ Here are the chats you allowed permission for play:**\n\n{txt}")
    await message.reply('No chats have play commands permission ❌')

queue = {}
is_playing = {}

async def play(message, number):
    global is_playing
    try:
        if is_playing.get(message.chat.id) and not vcInfo.get(message.chat.id+number): return
        try: await SophiaVC.start()
        except: pass
        is_playing[message.chat.id] = True
        data = vcInfo.get(message.chat.id+number)
        title, dur = data.title, data.duration
        type, path, thumb = data.type, data.path, data.thumb
        await message.reply_photo(
            photo=thumb,
            caption=(
                f"**✅ Started Streaming On VC.**\n\n"
                f"**🥀 Title:** {title[:20] if len(title) > 20 else title}\n"
                f"**🐬 Duration:** {dur // 60}:{dur % 60:02d} Mins\n"
                f"**🦋 Stream Type:** {type}\n"
                f"**👾 Requested By:** {message.from_user.first_name if not message.from_user.last_name else f'{message.from_user.first_name} {message.from_user.last_name}'}\n"
                f"**⚕️ Join:** __@Hyper_Speed0 & @FutureCity005__"
            )
        )
        await SophiaVC.play(message.chat.id, MediaStream(path))
        await asyncio.sleep(dur + 5)
        if queue.get(number+1):
            del vcInfo[message.chat.id+number]
            data = vcInfo[message.chat.id+number+1]
            await play(data.message, number+1)
        else:
            is_playing[message.chat.id] = False
            await SophiaVC.leave_call(message.chat.id)
    except Exception as e:
        if str(e) == """Telegram says: [403 CHAT_ADMIN_REQUIRED] - The method requires chat admin privileges (caused by "phone.CreateGroupCall")""":
            return await message.reply('**Cannot play song admin rights required ❌**')
        e = traceback.format_exc()
        logging.error(e)
        return await message.reply(f"Error: {e}")

@bot.on_message(filters.command(["play", "sp"], prefixes=PLAYPREFIXES) & filters.create(publicFilter) & ~filters.private & ~filters.bot)
async def play_(_, message):
    global vcInfo, queue
    try: await SophiaVC.start()
    except: pass
    if len(message.text.split()) < 2:
        if message.reply_to_message and message.reply_to_message.audio:
            try:
                m = await message.reply("📥 Downloading...")
                file = message.reply_to_message.audio
                path = await message.reply_to_message.download()
                title = file.title or file.file_name or "Unknown Title"
                dur = file.duration or 0
                await m.delete()
                if queue.get(message.chat.id): queue[message.chat.id] += 1
                else: queue[message.chat.id] = 1
                vcInfo[int(message.chat.id)+queue[message.chat.id]] = {
                    "title": f'{title} {message.id}',
                    "duration": dur,
                    "type": "Telegram audio",
                    "path": path,
                    "thumb": "https://i.imgur.com/9KKPfOA.jpeg",
                    "message": message 
                }
                await play(message, queue[message.chat.id])
            except:
                e = traceback.format_exc()
                await message.reply(f"Error: {e}")
                return logging.error(e)
            return
        else: return await message.reply("Provide a song name or link.")
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
        except: return await m.edit("⚠️ No results were found.")
    s_title = re.sub(r'[<>:"/\\|?*]', '_', title)
    thumb_name = f"{s_title}.jpg"
    if thumbnail:
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
    await m.edit("📥 Downloading...")
    try:
        ydl_opts = {"format": "bestaudio[ext=m4a]", "cookiefile": "cookies.txt"}
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            audio_file = ydl.prepare_filename(info_dict)
        secmul, dur, dur_arr = 1, 0, str(duration).split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        await m.delete()
        if queue.get(message.chat.id): queue[message.chat.id] += 1
        else: queue.get[message.chat.id] = 1
        vcInfo[message.chat.id+queue[message.chat.id]] = {
            "title": f'{title} {message.id}',
            "duration": dur,
            "type": "Audio",
            "path": audio_file,
            "thumb": thumb_name,
            "message": message 
        }
        await play(message, queue[message.chat.id])
    except:
        e = traceback.format_exc()
        logging.error(e)
        await message.reply(f"Error: {e}")
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except: pass

@bot.on_message(filters.command("vplay", prefixes=PLAYPREFIXES) & filters.user(OWN) & ~filters.private & ~filters.bot)
async def vplay(_, message):
    """
    global vcInfo, queue
    if len(message.text.split()) < 2:
        if message.reply_to_message and message.reply_to_message.video:
            try:
                m = await message.reply("📥 Downloading...")
                file = message.reply_to_message.video
                path = await message.reply_to_message.download()
                file_name = file.file_name or "Unknown Title"
                title = file_name
                dur = int(file.duration or 0)
                await m.delete()
                await message.reply_photo(
                    photo="https://i.imgur.com/9KKPfOA.jpeg",
                    caption=f"**✅ Started Streaming On VC.**\n\n**🥀 Title:** {title[:20] if len(title) > 20 else title}\n**🐬 Duration:** {dur // 60}:{dur % 60:02d} Mins\n**🦋 Stream Type:** Telegram video\n**👾 Requested By:** {message.from_user.first_name if not message.from_user.last_name else f'{message.from_user.first_name} {message.from_user.last_name}'}\n**⚕️ Join:** __@Hyper_Speed0 & @FutureCity005__"
                )
                vcInfo[message.chat.id] = {"title": f'{title} {message.id}', "duration": dur}
                await SophiaVC.play(message.chat.id, MediaStream(path))
                await manage_playback(message.chat.id, f'{title} {message.id}', dur)
            except Exception as e:
                await message.reply(f"Error: {e}")
                return logging.error(e)
            return
        else: return await message.reply("Provide a video name or link.")
    query = " ".join(message.command[1:])
    m = await message.reply("🔄 Searching....")
    if query.startswith(("www.youtube", "http://", "https://")):
        link = query
        with YoutubeDL({'quiet': True, 'noplaylist': True}) as ydl:
            info = ydl.extract_info(link, download=False)
            title = info.get("title", "Unknown Title")
            thumbnail = info.get("thumbnail")
            duration = int(info.get("duration", 0))
            is_video = True 
    else:
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            link = f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = int(results[0]["duration"].split(":")[0]) * 60 + int(results[0]["duration"].split(":")[1])
            is_video = True
        except: return await m.edit("⚠️ No results were found.")
    s_title = re.sub(r'[<>:"/\\|?*]', '_', title)
    thumb_name = f"{s_title}.jpg"
    if thumbnail:
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
    await m.edit("📥 Downloading...")
    try:
        ydl_opts = {
            "format": "worstvideo[ext=mp4]+bestaudio/best" if is_video else "bestaudio[ext=m4a]",
            "cookiefile": "cookies.txt"
        }
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            video_file = ydl.prepare_filename(info_dict)
        await m.delete()
        await message.reply_photo(
            photo=thumb_name,
            caption=f"**✅ Started Streaming On VC.**\n\n**🥀 Title:** {title[:20] if len(title) > 20 else title}\n**🐬 Duration:** {duration // 60}:{duration % 60:02d} Mins\n**🦋 Stream Type:** Video\n**👾 Requested By:** {message.from_user.first_name if not message.from_user.last_name else f'{message.from_user.first_name} {message.from_user.last_name}'}\n**⚕️ Join:** __@Hyper_Speed0 & @FutureCity005__"
        )
        vcInfo[message.chat.id] = {"title": f'{title} {message.id}', "duration": duration}
        await SophiaVC.play(message.chat.id, MediaStream(video_file))
        await manage_playback(message.chat.id, f'{title} {message.id}', duration)
    except Exception as e:
        await message.reply(f"Error: {e}")
        return logging.error(e)
    try:
        os.remove(video_file)
        os.remove(thumb_name)
    except: pass"""
        
@bot.on_message(filters.command("skip", prefixes=PLAYPREFIXES) & filters.create(publicFilter) & ~filters.private & ~filters.bot)
async def skip(_, message):
    """
    try:
        await message.delete()
    except:
        pass
    if vcInfo.get(message.chat.id):
        try:
            
            vcInfo.pop(message.chat.id, None)
        except Exception as e:
            await message.reply('Nothing streaming in vc ❌')
    else:
        await message.reply('Nothing streaming in vc ❌')"""

MOD_NAME = "Play"
MOD_HELP = """**🥀 Your commands**:
.play - To play a song in voice chat
.vplay - To play a youtube video on voice chat
.skip - To skip a playing song/video
.addplay - To allow a chat to use GroupUsers commands
.rplay - To remove permission of a chat to use GroupUsers commands
.getplay - To get allowed permission chats of GroupUsers commands

**👤 GroupUsers commands**:
.play - To play a song in voice chat
.skip - To skip a playing song/video
"""
