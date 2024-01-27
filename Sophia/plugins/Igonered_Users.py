from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID, IGNORED_USERS_ID
from pyrogram import filters
import asyncio

warning_count = {}

@Sophia.on_message(filters.private & filters.user(IGNORED_USERS_ID))
async def ignored_chat(_, message):
    Name_get = await Sophia.get_me()
    Name = Name_get.first_name
    user_id = message.from_user.id

    await message.reply_text(f"I ᴀᴍ ɴᴏᴛ {Name}, ɪ'ᴍ Sᴏᴘʜɪᴀ ᴀ Vɪʀᴜᴛᴀʟ Assɪsᴛᴀɴᴛ. Fᴏʀ {Name},\n ʜᴇ/sʜᴇ Iɢɴᴏʀᴇᴅ ʏᴏᴜ sᴏ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴄʜᴀᴛ ᴡɪᴛʜ ʜɪᴍ/ʜᴇʀ ❌")

    # Check if the user has been warned before
    if user_id not in warning_count:
        warning_count[user_id] = 1
    else:
        warning_count[user_id] += 1

    # Warn the user
    if warning_count[user_id] == 1:
        await Sophia.send_message(user_id, "Sᴏʀʀʏ, ɪ ᴄᴀɴ'ᴛ ᴅᴏ Aɴʏᴛʜɪɴɢ Aғᴛᴇʀ Yᴏᴜ Sᴇɴᴛ ᴍᴇ Aɴᴏᴛʜᴇʀ Msɢ. Bᴄᴢ. ɪ ᴡɪʟʟ Bʟᴏᴄᴋ Yᴏᴜ 💯 (IT'S RULE I CAN'T BREAK IT)")
    elif warning_count[user_id] == 2:
        await Sophia.send_message(user_id, "This is your second warning. If you send another message, you will be blocked.")
    elif warning_count[user_id] >= 3:
        try:
            # Archive the chat and block the user
            await Sophia.archive_chat(message.chat.id)
            await Sophia.block_user(user_id)
        except Exception as e:
            print(e)
            await Sophia.send_message(OWNER_ID, f"Sorry Master, I got an error when archiving and blocking Ignored User. Check Errors Below 💔\n {e}")
