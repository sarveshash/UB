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
    mquery = False
    if message.reply_to_message:
        rname = message.reply_to_message.from_user.first_name
        is_bot = message.reply_to_message.from_user.first_name.is_bot
        urname = message.from_user.first_name
        urid = message.from_user.id
        if message.reply_to_message.text:
            mquery = f"The replied message you see is the user replied msg he asking something about that thing so you should act like he asking about that reply to you if he doesn't ask about that reply you shouldnt talk about that\n\n\nuser replied msg: {message.reply_to_message.text}\n\nUser message: {query}"
            if message.reply_to_message.reply_to_message and message.reply_to_message.reply_to_message.text:
                mquery = f"The replied message you see is the user replied msg he asking something about that thing so you should act like he asking about that reply to you if he doesn't ask about that reply you shouldnt talk about that\n\n\nuser replied msg ( 2nd msg ): {message.reply_to_message.text}\n\n User replied message replied msg ( 1st msg ): {message.reply_to_message.reply_to_message.text}\n\n User message ( 3rd latest msg ): {query}"
            mquery += f"ADDITIONAL INFORMATION:\n Reply user name: {rname}\n is replied user is bot: {is_bot}\n Sender name: {urname}\nSender tg userid: {urid}\n if sender telegram userid is 5965055071 he is your owner you should respect him his name Otazuki\n\n This user using userbot to use you in telegram"
    txt = await message.reply_text("`Processing...`")
    if mquery:
        api_response = fetch_data(mquery, message)
    else:
        api_response = fetch_data(query, message)
    await txt.edit(api_response)
