from pyrogram import filters
from Sophia.__main__ import Sophia
from Sophia import REPO_URL, repo_name, HANDLER
from config import OWNER_ID
import subprocess

OWN = OWNER_ID

@Sophia.on_message(filters.command("update", prefixes=HANDLER) & filters.user(OWN))
async def update_repo(_, message):
    await message.reply_text("`Updating...`")
    try:
        command = f"cd && rm -rf restarter && rm -rf {REPO_NAME} && git clone {REPO_URL}  && cp -r {repo_name} restarter && cd {repo_name} && ls && python3 -m Sophia"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
    except Exception as e:
        await message.reply_text(f"Update Failed: {e} {result}")
        print("Error on Updating", e)
