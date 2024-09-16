from pyrogram import filters
from Sophia.__main__ import Sophia
from Sophia import REPO_URL, repo_name, HANDLER
from config import OWNER_ID
from subprocess import getoutput as run

OWN = OWNER_ID

@Sophia.on_message(filters.command("update", prefixes=HANDLER) & filters.user(OWN))
async def update_repo(_, message):
    await message.reply_text("`Updating...`")
    result = await run(f"cd && rm -rf {repo_name} && git clone {repo_name}  && cd {repo_name} && ls && python3 -m Sophia")
    await message.reply_text(f"Update Failed: {result}")
    print("Error on Updating", e)
