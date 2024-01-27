from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID, IGNORED_USERS_ID
from pyrogram import filters
import asyncio
import os

@Sophia.on_message(filters.user(IGNORED_USERS_ID))
async def Ignored_chat(_, message):
    Name_get = await Sophia.get_me()
    Name = Name_get.first_name
    await message.reply_text("I ᴀᴍ ɴᴏᴛ {Name}, ɪ'ᴍ Sᴏᴘʜɪᴀ ᴀ Vɪʀᴜᴛᴀʟ Assɪsᴛᴀɴᴛ. Fᴏʀ {Name},\n ʜᴇ/sʜᴇ Iɢɴᴏʀᴇᴅ ʏᴏᴜ sᴏ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴄʜᴀᴛ ᴡɪᴛʜ ʜɪᴍ/ʜᴇʀ ❌")
    try:
        await Sophia.archive_chat(message.chat.id)
    except Exception as e:
        print(e)
        await Sophia.send_message(OWNER_ID, f"Sorry Master, I got Error When Archiving Ignored User. Check Errors Below 💔\n {e}")
    @Sophia.on_message()
    async def Warn_to_block(_, message):
        await message.reply("Sᴏʀʀʏ, ɪ ᴄᴀɴ'ᴛ ᴅᴏ Aɴʏᴛʜɪɴɢ Aғᴛᴇʀ Yᴏᴜ Sᴇɴᴛ ᴍᴇ Aɴᴏᴛʜᴇʀ Msɢ. Bᴄᴢ. ɪ ᴡɪʟʟ Bʟᴏᴄᴋ Yᴏᴜ 💯 (IT'S RULE I CAN'T BREAK IT)")
        @Sophia.on_message()
        async def Just_Block_That_Baka(_, message):
            await message.reply("Nothing Just Block")
            await Sophia.block_user(message.chat.id)
