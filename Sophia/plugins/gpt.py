import requests
from pyrogram import filters, Client
from pyrogram.types import Message
from Sophia.__main__ import Sophia as app
from config import OWNER_ID
from Sophia import HANDLER
import json

def fetch_data(query: str, message: str) -> tuple:
    try:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json"
        }
        url =  "https://api.binjie.fun/api/generateStream"
        data = {
            "prompt": query,
            "userId": "#/chat/1722576084617",
            "network": True,
            "stream": False,
            "system": {
                "userId": "#/chat/1722576084617",
                "withoutContext": False
            }
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        data = response.text
        return data
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.on_message(filters.command(["chat", "gpt"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def chatgpt(_: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Please provide a query.")
    query = " ".join(message.command[1:])
    txt = await message.reply_text("`Processing...`")
    api_response = fetch_data(query, message)
    await txt.edit(api_response)
