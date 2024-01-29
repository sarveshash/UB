from pyrogram import filters
from config import OWNER_ID
from Sophia import HANDLER
from Sophia.__main__ import Sophia


@Sophia.on_message(filters.command(["cinfo", "channelinfo"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def cinfo(_, m):
    reply = m.reply_to_message
    if not reply:
        await m.reply_text("yoo! baka reply to channel")
        return
    if not reply.sender_chat:
        await m.reply_text("yoo! baka reply to channel")
        return
    if reply.sender_chat:
        message = await m.reply_text("information gathering!!!")
        id = reply.sender_chat.id
        reply.sender_chat.type
        name = reply.sender_chat.title
        username = reply.sender_chat.username
        pfp = reply.sender_chat.photo
    if not pfp:
        text = f"✪ **TYPE:** Channel\n\n"
        text += f"✪ **ID:** {id}\n\n"
        text += f"✪ **NAME:** {name}\n\n"
        text += f"✪ **USERNAME:** @{username}\n\n"
        text += f"✪ **MENTION:** [link](t.me/{username})"
        await m.reply_text(text)
        await message.delete()
        return
    image = reply.sender_chat.photo
    if image:
        photo = await Sophia.download_media(image.big_file_id)
        text = f"✪ **TYPE:** Channel\n\n"
        text += f"✪ **ID:** {id}\n\n"
        text += f"✪ **NAME:** {name}\n\n"
        text += f"✪ **USERNAME:** @{username}\n\n"
        text += f"✪ **MENTION:** [link](t.me/{username})"
        await m.reply_photo(photo=photo, caption=(text))
        await message.delete()


no_reply_user = """ ╒═══「 Appraisal results:」

**ɪᴅ**: `{}`
**ᴅᴄ**: `{}`
**ғɪʀsᴛ ɴᴀᴍᴇ**: {}
**ᴜsᴇʀɴᴀᴍᴇ**: @{}
**ᴘᴇʀᴍᴀʟɪɴᴋ**: {}
**ᴜsᴇʀʙɪᴏ**: {}

**Powered by: @Hyper_Speed0 & @FutureCity005 ✨🥀**
"""


@Sophia.on_message(filters.command("info", prefixes=HANDLER) & filters.user(OWNER_ID))
async def info(_, m):
    m.reply_to_message
    if not message.reply_to_message:
        await m.reply_text("Master, Please Reply to a User!")
        return
    id_user = m.reply_to_message.from_user.id
    msg = await m.reply_text("`Processing...`")
    info = await Sophia.get_chat(id_user)
    if info.photo:
        file_id = info.photo.big_file_id
        photo = await Sophia.download_media(file_id)
        user_id = info.id
        first_name = info.first_name
        username = info.username
        user_bio = info.bio
        dc_id = info.dc_id
        user_link = f"[link](tg://user?id={user_id})"
        await m.reply_photo(
            photo=photo,
            caption=no_reply_user.format(
                user_id, dc_id, first_name, username, user_link, user_bio
            ),
        )
    elif not info.photo:
        user_id = info.id
        first_name = info.first_name
        username = info.username
        user_bio = info.bio
        dc_id = info.dc_id
        user_link = f"[link](tg://user?id={user_id})"
        await m.reply_text(
            text=no_reply_user.format(
                user_id, dc_id, first_name, username, user_link, user_bio
            )
        )
    await msg.delete()
      
