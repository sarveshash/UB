import os
import sys
import requests
import logging
from pyrogram import *
from pymongo import MongoClient
from urllib.parse import urlparse
from motor.motor_asyncio import AsyncIOMotorClient
from subprocess import getoutput as r
from variables import *
import asyncio
from pytgcalls import PyTgCalls
from datetime import datetime
from Restart import restart_program as rs_pg

# LOGGING
logging.basicConfig(
    format="[Sophia-Beta] %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

# DATABASE
MONGO_DB_URI = os.environ.get("MONGO_DB_URI") or VAR_MONGO_DB_URI
if not MONGO_DB_URI:
    logging.error("Where is mongodb uri")
    exit()
MONGO_DB = MongoClient(MONGO_DB_URI) # Special Thanks To KoraXD For Giving This Codes!!
DATABASE = AsyncIOMotorClient(MONGO_DB_URI)["LinkUp"]
DB = DATABASE['SophiaInfo']
GAME_DATABASE = AsyncIOMotorClient(MONGO_DB_URI)["LinkUp"]

# Db session ( ignore )
try:
    dbSession = None
    async def something():
        global dbSession
        dbSession = await DB.find_one({"_id": 143})
        if dbSession and 'session' in dbSession:
            dbSession = dbSession['session']
        else: dbSession = None
    loop = asyncio.get_event_loop()
    loop.run_until_complete(something())  
except Exception as e:
    logging.error(e)
    pass

# VARIABLES
SESSION = os.environ.get("SESSION") or VAR_SESSION or dbSession
API_ID = os.environ.get("API_ID") or VAR_API_ID
API_HASH = os.environ.get("API_HASH") or VAR_API_HASH
HANDLER = [".","~","!","$","#"]
LOG_CHANNEL = -1002010994783
TOKEN = os.environ.get("TOKEN") or VAR_TOKEN
REPO_URL = os.environ.get("YOUR_REPO_LINK") or VAR_REPO_URL
MY_VERSION = 1.2
bot_start_time = datetime.now()
python_version = r('python --version').lower().replace('python ', '')
release_type = 'beta'
what_is_new = f"""Update {MY_VERSION} changelog:\n
1. Added queue on .play
2. Enhanced .help
3. Added .whisper
4. Added .bug To report a bug
5. Added .stats
6. Added settings
7. Bug fixes, Etc
"""
if not SESSION or not API_ID or not API_HASH or not MONGO_DB_URI or not REPO_URL or not TOKEN:
    raise "Values not found"
    logging.error("You should enter the required details on variables.py or you need set env")
    exit()

# PRINT STUFFS
logging.info(f"Loaded version: {MY_VERSION}")

# GETTING REPO NAME USED FOR UPDATE MODULE
parsed_url = urlparse(REPO_URL)
path_parts = parsed_url.path.split('/')
repo_name = path_parts[2] if len(path_parts) > 2 else None

# CLIENT
Sophia = Client("Sophia", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Sophia/plugins"))
if len(TOKEN) > 50: SophiaBot = Client("SophiaBot", session_string=TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Sophia/plugins"))
else: SophiaBot = Client("SophiaBot", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Sophia/plugins"))
SophiaVC = PyTgCalls(Sophia)

# Functions
def qfilter(inlineQuery):
    async def funcMano(_, __, query):
        try: return str(query.query).startswith(inlineQuery)
        except: return str(query.data).startswith(inlineQuery)
    return filters.create(funcMano)
