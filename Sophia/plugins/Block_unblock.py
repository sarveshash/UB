from Sophia import HANDLER
from Sophia.__main__ import Sophia
from pyrogram import filters
import asyncio
import os
from pyrogram import enums

@Sophia.on_message(filters.command("block", prefixes=HANDLER) & filters.me)
async def block_user(_, message):
    if message.chat.type == enums.ChatType.PRIVATE:
        try:
            await Sophia.block_user(message.chat.id)
            await message.reply("➲ I successfully blocked the user ✅.")
        except Exception as e:
            await message.reply("ERROR", e)
    else:
        if message.chat.type == enums.ChatType.SUPERGROUP:
            if not message.reply_to_message:
                return await message.reply("➲ Reply a user to block.")
            user_id = message.reply_to_message.from_user.id
            try:
                await Sophia.block_user(user_id)
                await message.reply("➲ I successfully blocked the user ✅.")
            except Exception as e:
                await message.reply("ERROR", e)


@Sophia.on_message(filters.command("unblock", prefixes=HANDLER) & filters.me)
async def unblock_user(_, message):
    if message.chat.type == enums.ChatType.SUPERGROUP:
        if not message.reply_to_message:
            return await message.reply("➲ Reply a user to unblock.")
        user_id = message.reply_to_message.from_user.id
        try:
            await Sophia.unblock_user(user_id)
            await message.reply("➲ I successfully unblocked the user ✅.")
        except Exception as e:
            await message.reply("ERROR", e)
    else:
        await message.reply("➲ This command Only works on Supergroups.")
        return
        
            
MOD_NAME = "Blocks"
MOD_HELP = ".block - Reply to a user or use in dm to block them.\n.unblock - Reply to a user or use in dm to unblock a user."
