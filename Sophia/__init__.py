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

# IDK
HM = "h"
if HM == None:
    OLD_DATAS_DB = input("Enter your mongodb uri: ") # For getting user values
    DATABASE = MongoClient(OLD_DATAS_DB)["SOPHIA_UB"]
    db = DATABASE["USER_DATAS"]
    Find = db.find_one({"_id": 404})
    if not Find:
        VALUES = None
    else:
        VALUES = Find
    if VALUES is not None:
        count = 0
        def inc_count():
            global count
            count += 1
        for ai_rule_world in VALUES:
            if count == 0:
                r(f"export SESSION={ai_rule_world}")
                inc_count()
            elif count == 1:
                r(f"export API_ID={ai_rule_world}")
                inc_count()
            elif count == 2:
                r(f"export API_HASH={ai_rule_world}")
                inc_count()
            elif count == 3:
                r(f"export MONGO_DB_URI={OLD_DATAS_DB}")
                inc_count()
            elif count == 4:
                r(f"export YOUR_REPO_LINK={ai_rule_world}")
                inc_count()
                rs_pg()
    while VALUES is None:
        try:
            while True:
                SESSION = input("Enter you Pyrogram V-2 Session: ")
                if len(SESSION) < 50:
                    print("[Sophia System] Enter session correctly!")
                else:
                    break
            API_ID = input("Enter Api ID: ")
            API_HASH = input("Enter Api hash: ")
            MONGO_DB_URI = input("Enter MONGO_DB_URI: ")
            YOUR_REPO_LINK = input("Enter your forked repo link: ")
            input("Enter to proceed: ")
            
            DATABASE = AsyncIOMotorClient(OLD_DATAS_DB)["SOPHIA_UB"]
            db = DATABASE["USER_DATAS"]
            doc = {"_id": 404, "SESSION": SESSION, "API_ID": API_ID, "API_HASH": API_HASH, "YOUR_REPO_LINK": YOUR_REPO_LINK, "everything": True}
            try:
                db.insert_one(doc)
            except Exception:
                db.update_one({"_id": 404}, {"$set": {"SESSION": SESSION, "API_ID": API_ID, "API_HASH": API_HASH, "YOUR_REPO_LINK": YOUR_REPO_LINK, "everything": True}})
            break
        except Exception as e:
            print(e)

# VARIABLES

SESSION = os.environ.get("SESSION")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
HANDLER = ["~",".","!","/","$","#"]
LOG_CHANNEL = -1002010994783
MONGO_DB_URI = os.environ.get("MONGO_DB_URI")
REPO_URL = os.environ.get("YOUR_REPO_LINK")
MY_VERSION = 0.5

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

# STARTING CLIENT
Sophia.start()
