import threading
from Sophia import *
from pyrogram import Client, filters
import os
from pyrogram import idle
from subprocess import getoutput as r
from Restart import restart_program
from others.restarted import is_restarted, restart_msg

PWD = f"{os.getcwd()}/"
my_id = None

if __name__ == "__main__":
    Sophia.start()
    if is_restarted:
        restart_msg.delete()
        a = Sophia.send_message(restart_msg.chat.id, "`Booting...`")
    SophiaBot.start()
    try:
        if 143 == 143:
            from config import OWNER_ID
            SophiaBot.send_photo(
                OWNER_ID,
                photo="https://i.imgur.com/DuoscLX.jpeg",
                caption=(
                    f"**✅ Sophia started ⚡**\n\n"
                    f"**👾 Version:** {MY_VERSION}\n"
                    f"**🥀 Python:** {r('python --version').lower().split('python ')[1]}\n"
                    f"**🐬 Owner:** {Sophia.me.first_name if not Sophia.me.last_name else f'{Sophia.me.first_name} {Sophia.me.last_name}'}\n"
                    f"**🦋 Join:** __@Hyper_speed0 & @FutureCity005__"
                )
            )
    except:
        pass
    if is_restarted:
        a.reply('Restart successful!')
        a.delete()
        with open("others/restarted.py", "w") as mano:
            ctx = "is_restarted = False\nrestart_msg = None"
            mano.write(ctx)
    idle()
