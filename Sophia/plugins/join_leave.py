from pyrogram import filters
from config import OWNER_ID
from Sophia import HANDLER
import re
from Sophia import Sophia

left_chat_id = ""

@Sophia.on_message(filters.command("join", prefixes=HANDLER) & filters.user(OWNER_ID))
def join_chat(_, m):
    global left_chat_id
    if len(m.command) < 2:
        m.reply_text("Master, Give a Group Username or id to Join")
        return
    link = m.text.split(" ")[1]
    if link.startswith("Back") or link.startswith("back"):
        if left_chat_id.startswith("-"):
            Sophia.join_chat(left_chat_id)
            chat = Sophia.get_chat(left_chat_id)
            name = chat.title
            Sophia.send_message(m.chat.id, f"Successfully Joined in {name}.")
            left_chat_id = ""
            return
        else:
            m.reply("No chats we left in recently.")
            return
    elif re.match("http", link, flags=re.IGNORECASE):
        link = link.split("/")[3]
    elif re.match("www", link, flags=re.IGNORECASE):
        link = link.split("/")[1]
        print("Link", link)
    try:
        Sophia.join_chat(link)
    except Exception as e:
        m.reply(f"Error, {e}")
        return
    chat = Sophia.get_chat(link)
    name = chat.title
    m.reply_text(f"Successfully joined in {name}.")


@Sophia.on_message(filters.command("leave", prefixes=HANDLER) & filters.user(OWNER_ID))
def leave_chat(_, m):
    global left_chat_id
    if len(m.command) < 2:
        m.reply_text("Master, Give Group username or id to leave it.")
        return
    link = m.text.split(" ")[1]
    if link.startswith("Here") or link.startswith("here"):
        left_chat_id = f"{m.chat.id}"
        chat = Sophia.get_chat(m.chat.id)
        name = chat.title
        Sophia.send_message(m.chat.id, f"Successfully left in {name}.")
        Sophia.leave_chat(m.chat.id)
        return
    elif re.match("http", link, flags=re.IGNORECASE):
        link = link.split("/")[3]
    elif re.match("www", link, flags=re.IGNORECASE):
        link = link.split("/")[1]
        print("Link", link)
    left_chat_id = f"{m.chat.id}"
    chat = Sophia.get_chat(link)
    name = chat.title
    try:
        Sophia.leave_chat(link)
        m.reply_text(f"Successfully left in {name}.")
    except Exception as e:
        m.reply(f"Error, {e}")
        print(e)
