from Sophia import *
from pyrogram import *
from pydub import AudioSegment
import speech_recognition as sr
from subprocess import getoutput as r
import time
from pyrogram import enums

@Sophia.on_message(filters.command('vtt', prefixes=HANDLER) & filters.user('me'))
async def voice_to_text(_, message):
    if not message.reply_to_message:
        return await message.reply('Please reply to an audio file to convert')
    if message.reply_to_message.media == enums.MessageMediaType.VOICE:
        await message.reply_to_message.download(file_name="voice_convert/output.mp3")
    elif message.reply_to_message.audio:
        await message.reply_to_message.download(file_name="voice_convert/output.mp3")
    elif message.reply_to_message.document.file_name.endswith(('.mp3', '.oga', '.wav', '.m4a')):
        await message.reply_to_message.download(file_name="voice_convert/output.mp3")
    else:
        return await message.reply("Please reply to a valid audio file!")
    edit_message = await message.reply("Converting audio to text...")
    audio = AudioSegment.from_file("voice_convert/output.mp3")
    audio.export("voice_convert/output_file.wav", format="wav")
    
    recognizer = sr.Recognizer()
    audio_file = "voice_convert/output_file.wav"
    
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    retries = 3
    delay = 1
    for attempt in range(retries):
        try:
            text = recognizer.recognize_google(audio_data)
            await edit_message.edit(f"```Text output\nOutput:\n{text}```")
            break
        except sr.UnknownValueError:
            await edit_message.edit("I cannot understand the audio!")
            break
        except sr.RequestError as e:
            if attempt < retries - 1:
                await edit_message.edit(f"Error: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                await message.reply(f"Failed to connect to Google Speech Recognition service after {retries} attempts.")
    
    await r("rm -rf voice_convert")
