from Sophia import *
from pyrogram import Client, filters
import os
import logging
import pyrogram

if __name__ == "__main__":
    ACCESS = decode_key(ACCESS_CODE, ACCESS_PIN)
    if ACCESS == "oTaZUki004nandhaiSgeY":
        Sophia.run()
    else:
        raise Exception("[INFO] Invalid Access Key, Access Key is required to Use Sophia Beta, Try Again")
        exit()
    
