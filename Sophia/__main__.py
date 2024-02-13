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
async def run_clients():
    await Sophia.start()
    await pm_guard_client.start()
    await pyrogram.idle()
    


if __name__ == "__main__":
    Sophia.loop.run_until_complete(run_clients())
