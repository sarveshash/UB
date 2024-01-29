from asyncio import sleep
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import MessageDeleteForbidden, RPCError
from Sophia.__main__ import Sophia as bot
from config import OWNER_ID
from Sophia import HANDLER

# Special Thanks For GitHub.com/BARATH-XD for Giving This Codes !!!

@bot.on_message(filters.command("purge", prefixes=HANDLER) & filters.user(OWNER_ID))
async def purge(_, m):
    if m.reply_to_message:
        message_ids = list(range(m.reply_to_message.id, m.id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await bot.delete_messages(
                    chat_id=m.chat.id,
                    message_ids=plist,
                    revoke=True,
                )
            await m.delete()
        except MessageDeleteForbidden:
            await m.reply_text("**Sorry**, I Cannot delete all messages. The messages may be too old, I might not have delete rights!.")
            return
        except Exception as ef:
            await m.reply_text(f"""Some error occured, Error: {ef}""")

        count_del_msg = len(message_ids)

        z = await m.reply_text(text=f"Successfully Deleted **{count_del_msg}** Messages...")
        await sleep(3)
        return
    await m.reply_text("Master, Please Reply to a message to start purge!")
