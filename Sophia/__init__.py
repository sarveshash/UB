import os
import sys
from pyrogram import Client

SESSION = os.environ.get("SESSION")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
HANDLER = ["~",".","!","/","$","#"]
MY_VERSION = 0.01
me = Sophia.get_me()
OWNER_USERNAME = me.username

# MAIN CLIENT OF SOPHIA
Sophia = Client("Sophia", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Sophia/plugins"))
