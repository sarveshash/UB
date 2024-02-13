from Sophia import *
from pyrogram import Client, filters
import os
import logging
import pyrogram

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

# Thanks To KoraXD for Giving Multiple Clients Run code
def run_clients():
    Sophia.start()
    pm_guard_client.run()
    pyrogram.idle()
    


if __name__ == "__main__":
    ACCESS = decode_key(ACCESS_CODE, ACCESS_PIN)
    if ACCESS == "oTaZUki004nandhaiSgeY":
        Sophia.loop.run_until_complete(run_clients())
        Sophia = Sophia
        pm_guard_client = pm_guard_client
        print("[INFO] Correct Access Key Bot Started")
    else:
        raise Exception("[INFO] Invalid Access Key, Access Key is required to Use Sophia Beta, Try Again")
        exit()
