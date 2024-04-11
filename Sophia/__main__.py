from Sophia import *
from pyrogram import Client, filters
import os
import io
import pyrogram
from subprocess import getoutput as run
from Restart import restart_program


PWD = f"{os.getcwd()}/"

# OWNER ID
me = Sophia.get_me()
id = me.id

if __name__ == "__main__":
    Sophia.run()
