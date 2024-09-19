try:
    from pyrogram import Client, filters
    from Sophia.__main__ import Sophia
    from Sophia import HANDLER
    import asyncio

    async def promote_user(chat_id, user_id, privileges):
        try:
            await Sophia.promote_chat_member(chat_id, user_id, **privileges)
            return True
        except Exception as e:
            print(f"Error promoting user {user_id}: {str(e)}")
            return False

    async def demote_user(chat_id, user_id):
        try:
            await Sophia.promote_chat_member(
                chat_id, user_id,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_manage_chat=False,
                can_manage_video_chats=False,
                can_manage_voice_chats=False,
                can_manage_media=False,
                can_manage_story=False,
                can_delete_messages=False
            )
            return True
        except Exception as e:
            print(f"Error demoting user {user_id}: {str(e)}")
            return False

    @Sophia.on_message(filters.command("fpromote", prefixes=HANDLER) & filters.user("me"))
    async def full_promote(_, message):
        me = await Sophia.get_me()
        me_id = me.id
    
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        else:
            if len(message.command) < 2:
                return await message.reply("Reply to a user or enter the user ID to promote.")
            user_id = str(message.text.split(None, 1)[1])
    
        if user_id == str(me_id):
            return await message.reply("You can't promote yourself!")
    
        privileges = {
            "can_change_info": True,
            "can_invite_users": True,
            "can_pin_messages": True,
            "can_manage_chat": True,
            "can_manage_video_chats": True,
            "can_manage_voice_chats": True,
            "can_manage_media": True,
            "can_manage_story": True,
            "can_delete_messages": True,
        }
    
        success = await promote_user(message.chat.id, user_id, privileges)
        if success:
            await message.reply(f"User with ID {user_id} has been promoted to full admin.")
        else:
            await message.reply(f"Failed to promote user with ID {user_id}.")

    @Sophia.on_message(filters.command("promote", prefixes=HANDLER) & filters.user("me"))
    async def normal_promote(_, message):
        me = await Sophia.get_me()
        me_id = me.id
    
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        else:
            if len(message.command) < 2:
                return await message.reply("Reply to a user or enter the user ID to promote.")
            user_id = str(message.text.split(None, 1)[1])
    
        if user_id == str(me_id):
            return await message.reply("You can't promote yourself!")
    
        privileges = {
            "can_change_info": False,
            "can_invite_users": True,
            "can_pin_messages": True,
            "can_manage_chat": True,
            "can_manage_video_chats": False,
            "can_manage_voice_chats": False,
            "can_manage_media": False,
            "can_manage_story": False
        }
    
        success = await promote_user(message.chat.id, user_id, privileges)
        if success:
            await message.reply(f"User with ID {user_id} has been promoted to normal admin.")
        else:
            await message.reply(f"Failed to promote user with ID {user_id}.")

    @Sophia.on_message(filters.command("lpromote", prefixes=HANDLER) & filters.user("me"))
    async def limited_promote(_, message):
        me = await Sophia.get_me()
        me_id = me.id
    
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        else:
            if len(message.command) < 2:
                return await message.reply("Reply to a user or enter the user ID to promote.")
            user_id = str(message.text.split(None, 1)[1])
    
        if user_id == str(me_id):
            return await message.reply("You can't promote yourself!")
    
        privileges = {
            "can_change_info": False,
            "can_invite_users": True,
            "can_pin_messages": False,
            "can_manage_chat": False,
            "can_manage_video_chats": False,
            "can_manage_voice_chats": False,
            "can_manage_media": False,
            "can_manage_story": True
        }
    
        success = await promote_user(message.chat.id, user_id, privileges)
        if success:
            await message.reply(f"User with ID {user_id} has been promoted to limited admin.")
        else:
            await message.reply(f"Failed to promote user with ID {user_id}.")

    @Sophia.on_message(filters.command("demote", prefixes=HANDLER) & filters.user("me"))
    async def demote(_, message):
        me = await Sophia.get_me()
        me_id = me.id
    
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        else:
            if len(message.command) < 2:
                return await message.reply("Reply to a user or enter the user ID to demote.")
            user_id = str(message.text.split(None, 1)[1])
    
        if user_id == str(me_id):
            return await message.reply("You can't demote yourself!")
    
        success = await demote_user(message.chat.id, user_id)
        if success:
            await message.reply(f"User with ID {user_id} has been demoted.")
        else:
            await message.reply(f"Failed to demote user with ID {user_id}.")
except Exception as e:
    e = f"Error on promote.py: {e}"
    raise e
