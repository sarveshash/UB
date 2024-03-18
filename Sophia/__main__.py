from Sophia import *
from pyrogram import Client, filters
import os
import logging
import pyrogram
from Restart import restart_program


logging.basicConfig(
    format="[Sophia] %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

PWD = f"{os.getcwd()}/"


if __name__ == "__main__":
    ACCESS = decode_key(ACCESS_CODE, ACCESS_PIN)
    if ACCESS == "oTaZUki004nandhaiSgeY":
        try:
            Sophia.run();
        except Exception as e:
            ErrorPrinter.run()
            with ErrorPrinter:
                ErrorPrinter.send_message("me", f"Error starting Sophia:\n\n{e}")
                ErrorPrinter.stop()
    else:
        raise Exception("[INFO] Invalid Access Key, Access Key is required to Use Sophia Beta, Try Again")
        exit()
