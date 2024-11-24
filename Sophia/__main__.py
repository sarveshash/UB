import asyncio
from Sophia import *
from pyrogram import Client, filters
import os
import io
from subprocess import getoutput as run
from Restart import restart_program

PWD = f"{os.getcwd()}/"
my_id = None

async def runn():
    global my_id
    await Sophia.start()
    my_id = await Sophia.get_me()
    my_id = my_id.id

    try:
        await Sophia.send_message(-1001859707851, "Sophia system started")
    except:
        await Sophia.join_chat(-1001859707851)
        await Sophia.send_message(-1001859707851, "Sophia system started")

    await Sophia.stop()
    return my_id

async def main():
    task = asyncio.create_task(runn())
    my_id = await task
    print(f"My ID is: {my_id}")
    await Sophia.run()

if __name__ == "__main__":
    asyncio.run(main())
