import threading
from Sophia import *
from pyrogram import Client, filters
import os
from subprocess import getoutput as run
from Restart import restart_program

PWD = f"{os.getcwd()}/"
my_id = None

if __name__ == "__main__":
    Sophia.run()
