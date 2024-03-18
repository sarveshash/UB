from Sophia import *
from pyrogram import Client, filters
import os
import io
import logging
import pyrogram
from subprocess import getoutput as run
from Restart import restart_program


logging.basicConfig(
    format="[Sophia] %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.basicConfig(filename='error.txt', level=logging.ERROR)

PWD = f"{os.getcwd()}/"


if __name__ == "__main__":
    ACCESS = decode_key(ACCESS_CODE, ACCESS_PIN)
    if ACCESS == "oTaZUki004nandhaiSgeY":
        try:
            otazukigcgv
            :;&(.
            hj
        except Exception as e:
            ErrorPrinter.run()
            with ErrorPrinter:
                run_logs = run("cat error.txt")
                if len(run_logs) >= 3000:
                    with io.BytesIO(str.encode(run_logs)) as logs:
                        logs.name = "ERROR.txt"
                        ErrorPrinter.send_document(
                            "me",
                            document=logs,
                            caption="ERROR STARTING SOPHIA",
                        )
                else:
                    ErrorPrinter.send_message("me", f"ERROR STARTING SOPHIA:\n\n```shell\n{run_logs}```")
                raise Exception(run_logs)
                ErrorPrinter.stop()
                    
    else:
        raise Exception("[INFO] Invalid Access Key, Access Key is required to Use Sophia Beta, Try Again")
        exit()
