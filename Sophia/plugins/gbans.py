from Sophia import HANDLER
from Sophia.__main__ import Sophia
from pyrogram import filters
import asyncio
import time
from pyrogram import enums, errors

async def ban_unban_user(message, action, user_id=None):
    me = (await Sophia.get_me()).id
    if user_id == me:
        return await message.reply("You can't perform this action on yourself!")

    success_chats = 0
    time_start = time.time()
    loading_msg = await message.reply(f"{'Starting gban' if action == 'ban' else 'Starting ungban'}! ⚡")

    async for dialog in Sophia.get_dialogs():
        if dialog.chat.type in [enums.ChatType.SUPERGROUP, enums.ChatType.GROUP]:
            try:
                if action == 'ban':
                    await Sophia.ban_chat_member(dialog.chat.id, user_id)
                else:
                    await Sophia.unban_chat_member(dialog.chat.id, user_id)
                success_chats += 1
                await asyncio.sleep(2)  # Avoid FloodWait
            except errors.ChatAdminRequired:
                print(f"Admin rights required in chat {dialog.chat.id}")
            except errors.FloodWait as e:
                print(f"Flood wait of {e.value} seconds")
                await asyncio.sleep(e.value)
            except Exception as e:
                print(f"Error in chat {dialog.chat.id}: {e}")

    await loading_msg.delete()
    await message.reply(f"{'Gban' if action == 'ban' else 'Ungban'} completed in {success_chats} chats\nTaken time: {int(time.time() - time_start)} seconds")


@Sophia.on_message(filters.command("gban", prefixes=HANDLER) & filters.user("me"))
async def gban(_, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) >= 2:
        try:
            user_id = int(message.command[1])
        except ValueError:
            return await message.reply("Please enter a valid user ID.")
    else:
        return await message.reply("Reply to a user or enter a valid user ID.")

    await ban_unban_user(message, action="ban", user_id=user_id)


@Sophia.on_message(filters.command("ungban", prefixes=HANDLER) & filters.user("me"))
async def ungban(_, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) >= 2:
        try:
            user_id = int(message.command[1])
        except ValueError:
            return await message.reply("Please enter a valid user ID.")
    else:
        return await message.reply("Reply to a user or enter a valid user ID.")

    await ban_unban_user(message, action="unban", user_id=user_id)
