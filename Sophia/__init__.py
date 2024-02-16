import os
import sys
from pyrogram import Client

SESSION = os.environ.get("SESSION")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
ACCESS_CODE = os.environ.get("ACCESS_CODE")
ACCESS_PIN = os.environ.get("ACCESS_PIN")
HANDLER = ["~",".","!","/","$","#"]
MY_VERSION = 0.01

# MAIN CLIENT OF SOPHIA
Sophia = Client("Sophia", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Sophia/plugins"))
# DATABASE CLIENT OF SOPHIA
Database = Client("Database", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Sophia/plugins"))

# DATABASE CACHE FILE TOTAL CODE

DATABASE_CACHE_CODE = """
approved_users = []
is_pm_block_enabled = False
maximum_message_count = 0


Reason_Of_Busy = {}
Does_Reason_Available = {}
approved_users = {}
Busy_stats = {}
"""

# BETA ACCESS KEY SECTION

ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def decode_key(encoded_key, pin):
    decoded_key = ''
    for char in encoded_key:
        if char.lower() in ALPHABET:  # Convert char to lowercase
            index = (ALPHABET.index(char.lower()) - int(pin)) % len(ALPHABET)
            decoded_key += ALPHABET[index]
        else:
            decoded_key += char
    return decoded_key
