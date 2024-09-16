"""from Sophia import *
from pyrogram import Client, filters
import os
import io
from Sophia.Database.update import UPDATE
import pyrogram
from subprocess import getoutput as run

def start_message():
    update_chk = UPDATE()
    update_chk = update_chk.GET()
    if update_chk is not False:
        Sophia.send_message(update_chk, "Successfully Updated")
        update_chk = UPDATE()
        update_chk.ADD(False, 0)
    Sophia.send_messags("me", "System Started")

try:
    start_message()
except Exception as e:
    print("Error when sending start msg:", e)"""
