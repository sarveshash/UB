# CODE RIGHTS RESERVED TO github.com/KoraXD ©
# API RIGHTS RESERVED TO t.me/Awesome_Tofu ™
import requests
from pyrogram import filters, Client
from pyrogram.types import Message, InputMediaPhoto
from Sophia import *
from config import OWNER_ID

api_url = "https://tofu-api.onrender.com/chat/bard"

def fetch_data(api_url: str, query: str) -> tuple:
    try:
        response = requests.get(f"{api_url}/{query}")
        response.raise_for_status()
        data = response.json()
        return data.get("content", "No response"), data.get("images", False)
    except requests.exceptions.RequestException as e:
        return None, f"Request error: {e}"
    except Exception as e:
        return None, f"Error: {str(e)}"

@Sophia.on_message(filters.command(["bard", "gemini"], HANDLER) & filters.user(OWNER_ID))
async def gemink(_, message):
    chat_id = message.chat.id
    message_id = message.id
    if len(message.command) < 2:
        return await message.reply_text("Please provide a query.")
    query = " ".join(message.command[1:])
    txt = await message.reply("💭")
    response_text, images = fetch_data(api_url, query)
    medias = []
    text = str(response_text)
    try:
       photo_url = images[-1]
    except:
        pass
    if images:
        if len(images) > 1:
            for url in images:
                medias.append(InputMediaPhoto(media=url, caption=None))
                        
            medias[-1] = InputMediaPhoto(media=photo_url, caption=text)
            
            try:
                await Sophia.send_media_group(chat_id=chat_id, media=medias, reply_to_message_id=message_id)
                return await txt.delete()
            except Exception as e:
                return await txt.edit(str(e))
        elif len(images) < 2:
            image_url = images[0]
            try:
                await message.reply_photo(photo=image_url, caption=text)
                return await txt.delete()
            except Exception as e:
                return await Sophia.send_message(LOG_CHANNEL, text)
        else:
            return await txt.edit('Something went wrong')
    else:
        try:
            return await txt.edit(text)
        except Exception as e:
            return await txt.edit(str(e))

# END
