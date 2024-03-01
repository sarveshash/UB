from Sophia import DATABASE, HANDLER, Sophia
from config import OWNER_ID
from pyrogram import filters
from pyrogram import enums

db = DATABASE["BACKUP_MESSAGE_TM"]

async def ENABLE_BACKUP():
    doc = {"_id": 1, "stats": True}
    try:
        await db.insert_one(doc)
    except Exception:
        await db.update_one({"_id": 1}, {"$set": {"stats": True}})
        
async def DISABLE_BACKUP():
    await db.update_one({"_id": 1}, {"$set": {"stats": False}})

async def GET_BACKUP():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return False
    else:
        stats = Find["stats"]
        return stats

async def ADD_BACKUP_CHAT(chat_id: int):
    await db.update_one({"_id": 1}, {"$addToSet": {"CHATS": chat_id}}, upsert=True)

async def REMOVE_BACKUP_CHAT(chat_id: int):
    await db.update_one({"_id": 1}, {"$pull": {"CHATS": chat_id}})

async def GET_BACKUP_CHATS():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return []
    else:
        value = Find.get("CHATS", [])
        return value

async def ADD_STOP_BACKUP_CHAT(chat_id: int):
    await db.update_one({"_id": 1}, {"$addToSet": {"STOPED_CHATS": chat_id}}, upsert=True)
    
async def REMOVE_STOP_BACKUP_CHAT(chat_id: int):
    await db.update_one({"_id": 1}, {"$pull": {"STOPED_CHATS": chat_id}})

async def GET_STOP_BACKUP_CHATS():
    Find = await db.find_one({"_id": 1})
    if not Find:
        return []
    else:
        value = Find.get("STOPED_CHATS", [])
        return value

async def SET_BACKUP_CHANNEL_ID(user_id, channel_id):
    await db.update_one({"_id": 1}, {"$set": {f"{user_id}": channel_id}})

async def GET_BACKUP_CHANNEL_ID(chat_id):
    Find = await db.find_one({"_id": 1})
    if not Find or str(chat_id) not in Find:
        return None
    else:
        channel = Find[str(chat_id)]
        return channel
    
async def REMOVE_BACKUP_CHANNEL_ID(user_id):
    await db.update_one({"_id": 1}, {"$unset": {f"{user_id}": ""}})
    await db.update_one({"_id": 1}, {"$pull": {"CHATS": user_id}})

async def backup_enabled(_, client, update):
    message = update
    if update.from_user.id == OWNER_ID:
        for x in HANDLER:
            if not len(update.text) < 2:
                if update.text.startswith(x) and update.from_user.id == OWNER_ID and await GET_BACKUP() and not update.chat.type == enums.ChatType.BOT:
                    return False
    if not await GET_BACKUP():
        return False
    else:
        if update.chat.id in await GET_STOP_BACKUP_CHATS():
            return False
        else:
            return True

@Sophia.on_message(filters.private & filters.create(backup_enabled) & ~filters.bot)
async def backup_chats(_, message):
    chat_id = await GET_BACKUP_CHANNEL_ID(message.chat.id)
    if chat_id is not None and chat_id == OWNER_ID and message.chat.id != OWNER_ID:
        try:
            if not message.chat.id == OWNER_ID and not message.chat.type == enums.ChatType.BOT:
                await Sophia.forward_messages(chat_id, message.chat.id, message.message_id)
        except Exception as e:
            if str(e) == """Telegram says: [400 CHANNEL_INVALID] - The channel parameter is invalid (caused by "channels.GetChannels")""":
                chat = await Sophia.create_channel(f"{message.chat.first_name} BACKUP", "~ @Hyper_Speed0")
                await ADD_BACKUP_CHAT(message.chat.id)
                await SET_BACKUP_CHANNEL_ID(message.chat.id, chat.id)
                await Sophia.forward_messages(chat.id, message.chat.id, message.message_id)
                await Sophia.archive_chats(chat.id)
                return
            else:
                print("Somthing went wrong in backup msg", e)
    else:
        if not message.chat.id == OWNER_ID and not message.chat.type == enums.ChatType.BOT:
            chat = await Sophia.create_channel(f"{message.chat.first_name} BACKUP", "~ @Hyper_Speed0")
            await ADD_BACKUP_CHAT(message.chat.id)
            await SET_BACKUP_CHANNEL_ID(message.chat.id, chat.id)
            await Sophia.forward_messages(chat.id, message.chat.id, message.message_id)
            await Sophia.archive_chats(chat.id)

@Sophia.on_message(filters.command(["resetbackup", "rbackup", "delbackup"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def delete_backup(_, message):
    if not message.chat.type == enums.ChatType.PRIVATE:
        return await message.reply("This command only works on Private chats")
    USERS = await GET_BACKUP_CHATS()
    if message.chat.id in USERS:
        CH = await GET_BACKUP_CHANNEL_ID(message.chat.id)
        try:
            await Sophia.delete_channel(CH)
            await REMOVE_BACKUP_CHANNEL_ID(message.chat.id)
            await message.reply("I have deleted this chat backup!")
            return
        except Exception as e:
            if str(e) == """Telegram says: [400 CHANNEL_INVALID] - The channel parameter is invalid (caused by "channels.GetChannels")""" or str(e) == """Peer id invalid: 0""":
                return await message.reply("This chat backup channel was already deleted.")
            return await message.reply(f"Error, {e}")
    else:
        return await message.reply("This chat has no backup!")
        
@Sophia.on_message(filters.command(["stopbackup", "sbackup"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def stop_backup(_, message):
    if not message.chat.type == enums.ChatType.PRIVATE:
        return await message.reply("This command Only works on Private chat")
    elif message.chat.id in await GET_STOP_BACKUP_CHATS():
        return await message.reply("This chat already stoped in backup")
    await ADD_STOP_BACKUP_CHAT(message.chat.id)
    await message.reply("I have stopped this chat from backup")

@Sophia.on_message(filters.command(["unstopbackup", "usbackup"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def unstop_backup(_, message):
    if not message.chat.type == enums.ChatType.PRIVATE:
        return await message.reply("This command Only works on Private chat")
    elif message.chat.id not in await GET_STOP_BACKUP_CHATS():
        return await message.reply("This chat is not stoped in backup")
    await REMOVE_STOP_BACKUP_CHAT(message.chat.id)
    await message.reply("I have unstopped this chat from backup")
