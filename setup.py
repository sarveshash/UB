import os
from subprocess import getoutput as r


SESSION = input("Enter you Pyrogram V-2 Session: ")
if len(SESSION) < 50:
    print("[Sophia System] Enter session correctly!")
    exit()
API_ID = input("Enter Api ID: ")
API_HASH = input("Enter Api hash: ")
ACCESS_CODE = input("Enter ACCESS_CODE: ")
ACCESS_PIN = input("Enter ACCESS_PIN: ")
MONGO_DB_URI = input("Enter MONGO_DB_URI: ")
YOUR_REPO_LINK = input("Enter your forked repo link: ")
input("Enter to proceed: ")

print("[INFO] Processing values...")

try:
  os.environ['SESSION'] = SESSION
  os.environ['API_ID'] = API_ID
  os.environ['API_HASH'] = API_HASH
  os.environ['ACCESS_CODE'] = ACCESS_CODE
  os.environ['ACCESS_PIN'] = ACCESS_PIN
  os.environ['MONGO_DB_URI'] = MONGO_DB_URI
  os.environ['YOUR_REPO_LINK'] = YOUR_REPO_LINK
except Exception as e:
  print(' ')
  raise e
  exit()

print("[INFO] Trying to Start Sophia..")
print("[INFO] Use next time 'python3 -m Sophia' Don't use setup.py!")
r("python3 -m Sophia")
