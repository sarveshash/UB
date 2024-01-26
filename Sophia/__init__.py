import os
import sys
from pyrogram import Client

SESSION = os.environ.get("SESSION")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
OWNER_ID = os.environ.get("OWNER_ID")
print(OWNER_ID)
HANDLER = ["~",".","!","/","$","#"]

Sophia = Client("Sophia", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Sophia/plugins"))
