from pyrogram import filters
from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID as OWN
from config import IGNORED_USERS_ID
from Restart import restart_program
import os
import re

me = Sophia.get_me()
OWNER_USERNAME = me.username

Busy_stats = {}

OWNUSR_ASLINK = f"https://t.me/{OWNER_USERNAME}"
OWNUSR_ASSHLINK = f"t.me/{OWNER_USERNAME}"
OWNUSR_ASNRML = f"@{OWNER_USERNAME}"

@Sophia.on_message(filters.command(["busy", "offline", "afk"], prefixes=HANDLER) & filters.user(OWN))
async def set_into_busy(_, message):
    global Busy_stats
    Busy_stats = True
    await message.reply_text("💖 **Master**, I Set You In Offline Mode I will Reply to everyone who wants to talk you, bye 👋")
    if Busy_stats == True:
        @Sophia.on_message(filters.private & ~filters.user(OWN))
        async def say_master_is_busy(_, message):
            if message.from_user.id == IGNORED_USERS_ID:
                return
            await message.reply_text("Huh, My **Master** Currently In **Offline** Can you Come **Later?**")
            @Sophia.on_message([OWNUSR_ASLINK, OWNUSR_ASSHLINK, OWNUSR_ASNRML, OWNER_USERNAME] & ~filters.user(OWN) & filters.group)
            async def Group_say_master_offline(_, message):
                if message.from_user.id == IGNORED_USERS_ID:
                    return
                await message.reply_text("Huh, My **Master** Currently In **Offline** Can you Come **Later?**")
                @Sophia.on_message(filters.user(OWN))
                async def remove_busy_mode(_, message):
                    await Sophia.send_message(OWN, "[INFO] you no longer in Offline mode")
                    await restart_program()
