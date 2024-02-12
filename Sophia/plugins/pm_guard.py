from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID, Always_Approved_Users_From_Pmblock
from pyrogram import filters
import asyncio
import os
from pyrogram import enums

is_pm_block_enabled = False
approved_users = {}
warning_count = []

@Sophia.on_message(filters.command(["pmblock", "pmguard"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def set_pm_guard(_, message):
    global is_pm_block_enabled
    if is_pm_block_enabled:
        is_pm_block_enabled = False
        await message.reply("I Disabled PmGuard Successfully ✅")
    else:
        is_pm_block_enabled = True
        await message.reply('PmGuard Has been Enabled ✅')
        return


@Sophia.on_message(filters.command(['a', 'approve'], prefixes=HANDLER) & filters.user(OWNER_ID))
async def Approve_user(_, message):
    if is_pm_block_enabled:
        if message.chat.type == enums.ChatType.SUPERGROUP:
            await message.reply("This Command Only Works On Private Chats.")
            return
        user_id = message.from_user.id
        try:
            approved_users.append(user_id)
            await message.reply("Successfully Approved ✅!")
        except Exception as e:
            await message.reply(f"Sorry, i got a error while approving this user\n\n{e}")
    else:
        if message.chat.type == enums.ChatType.SUPERGROUP:
            return
        await message.reply('`PmGuard Not Enabled ❌`')
        

@Sophia.on_message(~filters.user(OWNER_ID))
async def warn_users(_, message):
    if message.from_user.id in approved_users or message.from_user.id in Always_Approved_Users_From_Pmblock:
        return
    elif message.chat.type == enums.ChatType.SUPERGROUP:
        return
    if is_pm_block_enabled:
        user_id = message.from_user.id
        if user_id not in warning_count:
            warning_count[user_id] = 0
            
        warning_count[user_id] += 1
        # Warn the user
        if warning_count[user_id] == 1:
            await message.reply("Sorry, My master enabled Private Block Feature You can't Send message Now.")
        elif warning_count[user_id] == 2:
            await message.reply("This is your second warning. If you send Another message you will be blocked")
        elif warning_count[user_id] >= 3:
            try:
                await message.reply("You have breaked Your limits.")
                await Sophia.block_user(user_id)
            except Exception as e:
                print(e)
                await Sophia.send_message(OWN, e)
