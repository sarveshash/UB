import os
import sys
from pyrogram import Client
from config import MONGO_DB_URI
from pyrogram import Client
from pymongo import MongoClient
import motor.motor_asyncio

SESSION = os.environ.get("SESSION")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
ACCESS_CODE = os.environ.get("ACCESS_CODE")
ACCESS_PIN = os.environ.get("ACCESS_PIN")
HANDLER = ["~",".","!","/","$","#"]
MY_VERSION = 0.00219

# MAIN CLIENT OF SOPHIA
Sophia = Client("Sophia", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Sophia/plugins"))

# DATABASE OF SOPHIA
MONGO_DB = MongoClient(MONGO_DB_URI) # Special Thanks To KoraXD For Giving This Codes!!
DB = MONGO_DB.SOPHIA
DATABASE = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)

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
