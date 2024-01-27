from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID, IGNORED_USERS_ID
from pyrogram import filters

warning_count = {}

@Sophia.on_message(filters.private & filters.user(IGNORED_USERS_ID))
async def ignored_private_chat(_, message):
    user_id = message.from_user.id

    # Check if the user has been warned before
    if user_id not in warning_count:
        warning_count[user_id] = 0

    # Increment the warning count
    warning_count[user_id] += 1

    # Warn the user
    if warning_count[user_id] == 1:
        await message.reply("Sᴏʀʀʏ, Yᴏᴜ ᴀʀᴇ ɪɢɴᴏʀᴇᴅ ʙʏ ᴍʏ ʟᴏᴠᴇʟʏ ❤️ Mᴀsᴛᴇʀ, ɪғ ʏᴏᴜ sᴇɴᴅ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴀɢᴀɪɴ ʏᴏᴜ ᴡɪʟʟ ʙᴇ ɢᴇᴛ Bʟᴏᴄᴋᴇᴅ.")
        await Sophia.archive_chats([message.chat.id])
    elif warning_count[user_id] == 2:
        await message.reply("This is your second warning. If you send another message, you will be blocked.")
    elif warning_count[user_id] >= 3:
        try:
            await message.reply("Sorry, You Have Breaked Your Limits that's why I blocked You!")
            await Sophia.block_user(user_id)
            await Sophia.send_message(OWNER_ID, f"Master, I have Been Blocked A user From Ignored User List He/She Disturbing me i do that Hehe, If You Want Unblock Him/Her, Here is Username @{message.from_user.username}\n\n **Note:** If Want Clear all warn Do .restart or if you want remove him/her in ignore Remove This ID in your config.py Here is Id: `{message.from_user.id}`")
        except Exception as e:
            print(e)
            await Sophia.send_message(OWNER_ID, f"Sorry Master, I got an error when blocking Ignored User. Check Errors Below 💔\n {e}")
