from Sophia import *
from pyrogram import Client, filters
import os
import io
import pyrogram
from subprocess import getoutput as run
from Restart import restart_program

PWD = f"{os.getcwd()}/"

if __name__ == "__main__":
    try:
        Sophia.run()
    except Exception as e:
        print("Crashed:", e)
        print('Searching for backup file')
        try:
            run("cd && mv backup SophiaUB && cd SophiaUB && echo Update was failed Launching backup file && python3 -m Sophia")
        except:
            print("Backup file was not found")
            exit()
