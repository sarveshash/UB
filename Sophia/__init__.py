import os
import sys
import logging
from pyrogram import Client
from pyrogram import Client
from pymongo import MongoClient
from urllib.parse import urlparse
from motor.motor_asyncio import AsyncIOMotorClient
from subprocess import getoutput as r
from Restart import restart_program as rs_pg

# LOGGING
logging.basicConfig(
    format="[Sophia-UB] %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

# VARIABLES
SESSION = "BQCbcXYAgPaTnqIB-FAL2f82IDDVQbp9cr21B3vT70Mol6zGzx1CkmJUYhoGRYOc-UxeAU2IR9mDAdDDuaeL798asb9KmCUQDZG7rZNNuErDhnzDOePGpdvjj27t-acB1j7lEx3adRAYmln76xmy94uGkFoAcMQ-9zdrCXbmZZ-R00_Me4i5ZgVUvKFhQIPzWogeziLp-gzqo7DCBwI9YeaF8JbwMShmdhKHHwRjotEJS6C_VrSJBOx8ZkyglngEn3k27xRo6efc9SEIOYApi_dULv_2RETFmMrmJBw56VR-VhIDvAO0hoajTdhnq5YKXG2XLGBasKlp0mQ7pMpYf52YcpXYtAAAAAFji4RfAA"
API_ID = 10187126
API_HASH = "ff197c0d23d7fe54c89b44ed092c1752"
HANDLER = ["~",".","!","/","$","#"]
LOG_CHANNEL = -1002010994783
MONGO_DB_URI = "mongodb+srv://Wine_Music:red_wine55@cluster0.hbuxm0l.mongodb.net/?retryWrites=true&w=majority"
REPO_URL = "https://github.com/Otazuki004/SophiaUB/"
MY_VERSION = 0.00219

# GETTING REPO NAME USED FOR UPDATE MODULE
parsed_url = urlparse(REPO_URL)
path_parts = parsed_url.path.split('/')
repo_name = path_parts[2] if len(path_parts) > 2 else None

# CLIENTS
Sophia = Client("Sophia", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Sophia/plugins"))

# DATABASE OF SOPHIA
MONGO_DB = MongoClient(MONGO_DB_URI) # Special Thanks To KoraXD For Giving This Codes!!
DB = MONGO_DB.SOPHIA_UB
DATABASE = AsyncIOMotorClient(MONGO_DB_URI)["SOPHIA_UB"]
GAME_DATABASE = AsyncIOMotorClient(MONGO_DB_URI)["HYPER_GAMES"]
