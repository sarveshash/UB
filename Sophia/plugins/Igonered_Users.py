from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID, IGNORED_USERS_ID
from pyrogram import filters

warning_count = {}

@Sophia.on_message(filters.private & filters.user(IGNORED_USERS_ID))
async def ignored_private_chat(_, message):
    user_id = message.from_user.id
    if user_id not in warning_count:
        warning_count[user_id] = 0
    warning_count[user_id] += 1
    if warning_count[user_id] == 1:
        await message.reply("Sorry, you are a ignored person of my master you can't chat with him!")
        await Sophia.archive_chats([message.chat.id])
    elif warning_count[user_id] == 2:
        await message.reply("This is your second warning. If you send another message, you will be blocked.")
    elif warning_count[user_id] >= 3:
        try:
            await message.reply("Sorry, You have breaked your limits so i blocked you")
            await Sophia.block_user(user_id)
            await Sophia.send_message('me', f"Master, i have blocked {message.from_user.first_name}\n\nHe/she spamed in your chat so i blocked if you want unblock you can find them in archived chats! use .unignore to unignore them!")
        except Exception as e:
            print(e)
            await Sophia.send_message('me', f"Sorry Master, I got an error when blocking Ignored User. Check Errors Below 💔\n {e}")
