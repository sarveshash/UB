from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID, Always_Approved_Users_From_Pmblock
from pyrogram import filters
import asyncio
import os
from pyrogram import enums

is_pm_block_enabled = False
approved_users = []
warning_count = {}

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
    global approved_users
    if is_pm_block_enabled:
        if message.chat.type == enums.ChatType.SUPERGROUP:
            await message.reply("This Command Only Works On Private Chats.")
            return
        user_id = message.chat.id
        try:
            if user_id in approved_users:
                await message.reply('**This User is Already Approved ✨🥀**')
                return
            approved_users.append(user_id)
            await message.reply("Successfully Approved ✅⚡")
        except Exception as e:
            await message.reply(f"Sorry, i got a error while approving this user\n\n{e}")
    else:
        if message.chat.type == enums.ChatType.SUPERGROUP:
            return
        await message.reply('**PmGuard Not Enabled ❌**')


@Sophia.on_message(filters.command(['ua', 'unapprove'], prefixes=HANDLER) & filters.user(OWNER_ID))
async def Unapprove_user(_, message):
    global approved_users
    if is_pm_block_enabled:
        if message.chat.type == enums.ChatType.SUPERGROUP:
            await message.reply("This Command Only Works On Private Chats.")
            return
        user_id = message.chat.id
        try:
            approved_users.remove(user_id)
            await message.reply("Successfully Unapproved ✨🗿")
        except Exception as e:
            if str(e) == "list.remove(x): x not in list":
                await message.reply("**This user is Not Approved yet ❌**")
                return
            await message.reply(f"Sorry, i got a error while unapproving this user\n\n{e}")
    else:
        if message.chat.type == enums.ChatType.SUPERGROUP:
            return
        await message.reply('**PmGuard Not Enabled ❌**')
        
@Sophia.on_message(~filters.user(OWNER_ID) & filters.private)
async def warn_users(_, message):
    global approved_users, Always_Approved_Users_From_Pmblock, is_pm_block_enabled
    if is_pm_block_enabled:
        user_id = message.chat.id
        if user_id not in Always_Approved_Users_From_Pmblock and user_id not in approved_users:
            if user_id not in warning_count:
                warning_count[user_id] = 0
            warning_count[user_id] += 1
            if warning_count[user_id] == 1:
                await message.reply("Sorry, my master has enabled the PmGuard feature. You can't send messages until my master approves you or disables this feature. If you send a message again, you will be blocked.")
            elif warning_count[user_id] == 2:
                await message.reply("This is your second warning. If you send another message, you will be blocked.")
            elif warning_count[user_id] >= 3:
                try:
                    await message.reply("You have exceeded your limits, so I have blocked you!")
                    await Sophia.block_user(user_id)
                except Exception as e:
                    print(e)
                    await Sophia.send_message(OWNER_ID, e)
    else:
        pass  # Other functions will execute normally when is_pm_block_enabled is False
        
@Sophia.on_message(filters.command(['cw', 'clearwarns'], prefixes=HANDLER) & filters.user(OWNER_ID))
async def Clear_User_Warns(_, message):
    global warning_count
    if is_pm_block_enabled:
        if message.chat.type == enums.ChatType.SUPERGROUP:
            await message.reply("This Command Only Works On Private Chats.")
            return
        user_id = message.chat.id
        try:
            user_id = message.chat.id
            warning_count[user_id] = 0
            await message.reply("Successfully Cleared Warnings 🗿🔥")
        except Exception as e:
            await message.reply(f"Sorry, i got a error while Clearing Warns for this user\n\n{e}")
    else:
        if message.chat.type == enums.ChatType.SUPERGROUP:
            return
        await message.reply('**PmGuard Not Enabled ❌**')
                

#END
