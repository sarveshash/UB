from Sophia import *
from pyrogram import Client, filters
import os
from config import DATABASE_GROUP_ID
import logging
import pyrogram

FILE_AVAILABLE = False

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

PWD = f"{os.getcwd()}/"

def file_exists(file_path):
    return os.path.isfile(file_path)

async def run_clients():
    global FILE_AVAILABLE
    await Database.start()
    app = Database
    await app.send_message(-1001962303988, "Sophia started")
    async for message in app.search_messages(-1001962303988, query="#CACHE_FILE", limit=1):
        file_path = f"{PWD}Data.txt"
        try:
            await Database.download_media(message.document.file_id, file_name=file_path)
            if os.path.isfile(file_path):
                FILE_AVAILABLE = True
            else:
                FILE_AVAILABLE = False
        except Exception:
            if os.path.isfile(file_path):
                FILE_AVAILABLE = True
            else:
                FILE_AVAILABLE = False
            # Alien level coding be like .
    await Sophia.start()
    await pyrogram.idle()

if __name__ == "__main__":
    ACCESS = decode_key(ACCESS_CODE, ACCESS_PIN)
    if ACCESS == "oTaZUki004nandhaiSgeY":
        Sophia.loop.run_until_complete(run_clients())
    else:
        raise Exception("[INFO] Invalid Access Key, Access Key is required to Use Sophia Beta, Try Again")
        exit()
    
