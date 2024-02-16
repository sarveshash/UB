from Sophia import *
from pyrogram import Client, filters
import os
from config import DATABASE_GROUP_ID
import logging
import pyrogram

FILENOTFOUND = None

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
PWD = f"{os.getcwd()}/"
async def run_clients():
    await Database.start()
    app = Database
    await app.send_message(-1001962303988, "Sophia started")
    async for message in app.search_messages(-1001962303988, query="#CACHE_FILE", limit=1):
        try:
            await Database.download_media(message.document.file_id, file_name=f"{PWD}Data.txt")
        except AttributeError:
            FILENOTFOUND = True
    await Sophia.start()
    await pyrogram.idle()

if __name__ == "__main__":
    ACCESS = decode_key(ACCESS_CODE, ACCESS_PIN)
    if ACCESS == "oTaZUki004nandhaiSgeY":
        Sophia.loop.run_until_complete(run_clients())
    else:
        raise Exception("[INFO] Invalid Access Key, Access Key is required to Use Sophia Beta, Try Again")
        exit()
    
