from Sophia import *
from pyrogram import Client, filters
import os
import io
import pyrogram
from subprocess import getoutput as run
from Restart import restart_program

PWD = f"{os.getcwd()}/"
my_id = 0
async def runn():
    global my_id
    my_id = await Sophia.get_me()
    my_id = my_id.id


if __name__ == "__main__":
    asyncio.run(runn())
    Sophia.run()
