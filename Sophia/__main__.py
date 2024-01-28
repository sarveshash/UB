from Sophia import Sophia
from pyrogram import Client, filters
import os
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

me = Sophia.get_me()
OWNER_USERNAME = me.username

if __name__ == "__main__":
  Sophia.run()
  
