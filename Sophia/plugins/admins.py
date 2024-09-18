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
        id = str(message.text.split(None, 1)[1])
        if not id.isdigit() or not id.startswith('@'):
            return await message.reply("Please enter a valid id.")
        if id == me:
            return await message.reply("You can't ban yourself!")
        else:
            try:
                await Sophia.ban_chat_member(message.chat.id, id)
                await message.reply("Successfuly baned that nigga!")
            except Exception as e:
                e = str(e)
                if e.startswith("Telegram says: [400 PEER_ID_INVALID]"):
                    try:
                        m = await Sophia.send_message(id, ".")
                        await Sophia.ban_chat_member(message.chat.id, id)
                        m = m.delete()
                        await message.reply("Successfuly baned that nigga!")
                    except Exception as o:
                        return await message.reply(f"Error: {o}")
                await message.reply(f"Error: {e}")
