from Sophia import *
from pyrogram import Client, filters
import os
import io
from Sophia.Database.update import UPDATE
import pyrogram
from subprocess import getoutput as run
from Restart import restart_program

PWD = f"{os.getcwd()}/"

if __name__ == "__main__":
    Sophia.start()
    try:
        # START MESSAGE
        update_chk = UPDATE()
        update_chk = update_chk.GET()
        if update_chk is not False:
            Sophia.send_message(update_chk, "Successfully Updated")
            update_chk = UPDATE()
            update_chk.ADD(False, 0)
        Sophia.send_messags("me", "System Started")
    Sophia.idle()
