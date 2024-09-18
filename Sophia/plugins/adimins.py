from Sophia import *
from pyrogram import *

@Sophia.on_message(filters.command("ban", prefixes=HANDLER) & filters.user("me"))
async def ban(_, message):
    me = await Sophia.get_me()
    me = me.id
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == me:
            return await message.reply("You can't ban yourself!")
        else:
            try:
                await Sophia.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                await message.reply("Successfuly baned that nigga!")
            except Exception as e:
                await message.reply(f"Error: {e}")
    else:
        if len(message.command) < 2:
            return await message.reply_text("Reply a user or enter the user id to ban!")
        try:
            id = int(message.text.split(None, 1)[1])
            try:
                chk = str(id)
                if chk.startswith("-"):
                    return await message.reply("Please enter a user id")
            except Exception as e:
                raise e
        except:
            return await message.reply("Please enter a valid id.")
        if id == me:
            return await message.reply("You can't ban yourself!")
        else:
            try:
                await Sophia.ban_chat_member(message.chat.id, id)
                await message.reply("Successfuly baned that nigga!")
            except Exception as e:
                await message.reply(f"Error: {e}")
