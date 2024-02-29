from pyrogram import filters
from Sophia.__main__ import Sophia
from Sophia import REPO_URL, repo_name
from config import OWNER_ID
import subprocess

OWN = OWNER_ID

@Sophia.on_message(filters.command("update") & filters.user(OWN))
async def update_repo(_, message):
    await message.reply_text("`Updating...`")
    try:
        command = f"cd && rm -rf {repo_name} && git clone {REPO_URL} && cd {repo_name} && ls && python3 -m Sophia"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        exit()
    except Exception as e:
        await message.reply_text("Update Failed ", e)
        print("Error on Updating", e)
