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
    try:
        Sophia.start()
        Sophia.send_message("me", "hi da good")
    except Exception as e:
        print(e)
    Sophia.run()
