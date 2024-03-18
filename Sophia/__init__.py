import os
import sys
from pyrogram import Client
from pyrogram import Client
from pymongo import MongoClient
from urllib.parse import urlparse
from motor.motor_asyncio import AsyncIOMotorClient

SESSION = os.environ.get("SESSION")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
ACCESS_CODE = os.environ.get("ACCESS_CODE")
ACCESS_PIN = os.environ.get("ACCESS_PIN")
HANDLER = ["~",".","!","/","$","#"]
LOG_CHANNEL = -1002010994783
MONGO_DB_URI = os.environ.get("MONGO_DB_URI")
REPO_URL = os.environ.get("YOUR_REPO_LINK")
MY_VERSION = 0.00219

# GETTING REPO NAME USED FOR UPDATE MODULE
parsed_url = urlparse(REPO_URL)
path_parts = parsed_url.path.split('/')
repo_name = path_parts[2] if len(path_parts) > 2 else None

# CLIENTS
Sophia = Client("Sophia", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Sophia/plugins"))
ErrorPrinter = Client("ErrorPrinter", session_string=SESSION, api_id=API_ID, api_hash=API_HASH)

# DATABASE OF SOPHIA
MONGO_DB = MongoClient(MONGO_DB_URI) # Special Thanks To KoraXD For Giving This Codes!!
DB = MONGO_DB.SOPHIA_UB
DATABASE = AsyncIOMotorClient(MONGO_DB_URI)["SOPHIA_UB"]
GAME_DATABASE = AsyncIOMotorClient(MONGO_DB_URI)["HYPER_GAMES"]
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
