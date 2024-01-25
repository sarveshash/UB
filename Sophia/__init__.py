import os
import sys
from pyrogram import Client

SESSION = os.environ.get("STRING_SESSION")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
OWNER_ID = os.environ.get("OWNER_ID")


Sophia = Client(session_string=SESSION, api_id=API_ID, api_hash=API_HASH, name="Sophia")
UB = Sophia
system = Sophia
