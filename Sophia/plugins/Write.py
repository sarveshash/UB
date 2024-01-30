from pyrogram import filters
from config import SUDO_USERS_ID
from config import OWNER_ID
from Sophia import HANDLER
from Sophia.__main__ import Sophia


@Sophia.on_message(filters.command("write", prefixes=HANDLER) & filters.user(OWNER_ID))
async def write(_, message):
    if message.from_user.id == OWN or message.from_user.id in SUDO_USERS_ID:
        print("")
    else:
        return
    if len(message.command) < 2:
        return await message.reply_text("Mᴀsᴛᴇʀ, ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴛᴇxᴛ. ✨")
    m = await message.reply_text("Wʀɪᴛɪɴɢ...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("Uᴘʟᴏᴀᴅɪɴɢ...")
    await message.reply_photo(hand, caption="**Mᴀsᴛᴇʀ, ᴄᴀɴ ʏᴏᴜ ᴊᴏɪɴ ʜᴇʀᴇ?: @FutureCity005 & @Hyper_Speed0 🥀 ✨**")
    await m.delete()
  
