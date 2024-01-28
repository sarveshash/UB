from Sophia import Sophia, Sophia_StartMSG
from pyrogram import Client, filters
import os
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

if __name__ == "__main__":
  Sophia_StartMSG.start()
  with Sophia_StartMSG:
      Sophia_StartMSG.send_message(-1001859707851, "This Is Test Start msg of Sophia")
  Sophia_StartMSG.stop()
  Sophia.run()
  
