from Sophia import *
from pyrogram import Client, filters
import os
import io
from pytgcalls import *
import pyrogram
from subprocess import getoutput as run
from Restart import restart_program

PWD = f"{os.getcwd()}/"


if __name__ == "__main__":
    run("apt update && apt install -y default-jre && apt install -y default-jdk && apt install -y nodejs npm && nvm install node && curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash")
    Friday.idle()
    print("Friday started!")
    Sophia.run()
