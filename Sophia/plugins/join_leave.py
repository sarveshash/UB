from pyrogram import filters
from config import OWNER_ID
from Sophia import HANDLER
from Sophia import Sophia


@Sophia.on_message(filters.command("join", prefixes=HANDLER) & filters.user(OWNER_ID))
def join_chat(_, m):
    if len(m.command) < 2:
        m.reply_text("Master, Give a Group Username or ID to Join")
        return
    link = m.text.split(" ")[1]
    Sophia.join_chat(link)
    chat = Sophia.get_chat(link)
    name = chat.title
    m.reply_text(f"Successfully joined in {name}.")


@Sophia.on_message(filters.command("leave", prefixes=HANDLER) & filters.user(OWNER_ID))
def leave_chat(_, m):
    if len(m.command) < 2:
        m.reply_text("Master, Give Group username or id to leave it.")
        return
    link = m.text.split(" ")[1]
    Sophia.leave_chat(link)
    chat = Sophia.get_chat(link)
    name = chat.title
    m.reply_text(f"Successfully left in {name}.")
