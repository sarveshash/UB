from Sophia import HANDLER
from Sophia.__main__ import Sophia
from config import OWNER_ID
from pyrogram import filters
import asyncio
import os
import lyricsgenius

# Initialize the Genius API client with your access token
genius = lyricsgenius.Genius("OUa2UPIAPUeURuRVWMN9Gl0MoqsISggZBLbhCDtjshv1dZv9KZvh5jTJoPWlJnap")

@Sophia.on_message(filters.command("lyrics", prefixes=HANDLER) & filters.user(OWNER_ID))
async def search_lyrics(_, message):
    if len(message.text.split()) < 2:
        return await message.reply("Master, enter the name of the song to search for its lyrics.")
    MSG = await message.reply("Loading...")
    song_name = " ".join(message.command[1:])
    try:
        # Search for the song lyrics
        song = genius.search_song(song_name)
        if song is None:
            return await MSG.edit("Song not found.")
        await MSG.edit(f"Lyrics for '{song.title}' by {song.artist}:\n\n{song.lyrics}")
    except Exception as e:
        await MSG.edit(f"An error occurred: {e}")
