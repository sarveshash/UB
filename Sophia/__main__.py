import asyncio
from Sophia import *
from pyrogram import Client, filters
import os
import io
from subprocess import getoutput as run
from Restart import restart_program
from pytgcalls import idle

PWD = f"{os.getcwd()}/"
my_id = None

if __name__ == "__main__":
    idle()
    Sophia.run()
