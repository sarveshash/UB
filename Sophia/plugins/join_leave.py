from pyrogram import filters
from config import OWNER_ID
from Sophia import HANDLER
from Sophia import Sophia

left_chat_id = ""

@Sophia.on_message(filters.command("join", prefixes=HANDLER) & filters.user(OWNER_ID))
def join_chat(_, m):
    global left_chat_id
    if len(m.command) < 2:
        m.reply_text("Master, Give a Group Username or ID to Join")
        return
    link = m.text.split(" ")[1]
    if link.startswith("Back") or link.startswith("back"):
        if left_chat_id.startswith("-"):
            Sophia.join_chat(left_chat_id)
            chat = Sophia.get_chat(left_chat_id)
            name = chat.title
            Sophia.send_message(left_chat_id, f"Successfully Joined in {name}.")
            return
        else:
            m.reply("No chats we left in recently.")
            return
    Sophia.join_chat(link)
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
        Sophia.leave_chat(m.chat.id)
        chat = Sophia.get_chat(m.chat.id)
        name = chat.title
        Sophia.send_message(OWNER_ID, f"Successfully left in {name}.")
        return
    left_chat_id = f"{m.chat.id}"
    Sophia.leave_chat(link)
    chat = Sophia.get_chat(link)
    name = chat.title
    m.reply_text(f"Successfully left in {name}.")
