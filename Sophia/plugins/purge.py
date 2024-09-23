try:
    from pyrogram import filters
    from Sophia.__main__ import Sophia
    from Sophia import HANDLER
    import asyncio
    from pyrogram.enums import ChatType

    @Sophia.on_message(filters.command("purge", prefixes=HANDLER) & filters.user("me"))
    async def purge_messages(_, message):
        if message.chat.type.ChatType.PRIVATE:
            return await message.reply("This command is only works on group!")
        if not message.reply_to_message:
            return await message.reply("Reply to the first message you want to delete.")
        start_msg_id = message.reply_to_message.id
        end_msg_id = message.id
        success = 0
        breaked = False
        for msg_id in range(start_msg_id, end_msg_id + 1):
            try:
                await Sophia.delete_messages(message.chat.id, msg_id)
                success += 1
                await asyncio.sleep(0.3)
                if success >= 100:
                    break
                    breaked = True
            except Exception as e:
                print(f"Error deleting message {msg_id}: {str(e)}")
        if breaked:
            await message.reply("Successfuly purged 100 messages, I can only delete 100 try again!")
            breaked = False
            return
        await message.reply(f"Successfuly purged {success} messages!")
except Exception as e:
    e = f"Error on purge.py: {e}"
    raise e
