from Sophia import *
from pyrogram import *
from pydub import AudioSegment
import speech_recognition as sr
from subprocess import getoutput as r

@Sophia.on_message(filters.command('vtt', prefixes=HANDLER) & filters.user('me'))
async def voice_to_text(_, message):
    if not message.reply_to_message:
        return await message.reply('Please reply to a audio file to convert')
    if message.reply_to_message.media == "MessageMediaType.VOICE":
        await message.reply_to_message.download(file_name="voice_convert/output.mp3")
    elif message.reply_to_message.audio:
        await message.reply_to_message.download(file_name="voice_convert/output.mp3")
    elif message.reply_to_message.document.file_name.endswith('.mp3') or message.reply_to_message.document.file_name.endswith('.oga') or message.reply_to_message.document.file_name.endswith('.wav') or message.reply_to_message.document.file_name.endswith('.m4a'):
        await message.reply_to_message.download(file_name="voice_convert/output.mp3")
    else:
        return await message.reply("Please reply to a valid audio file!")
    
    audio = AudioSegment.from_file("voice_convert/output.mp3")
    audio.export("voice_convert/output_file.wav", format="wav")
    recognizer = sr.Recognizer()
    audio_file = "voice_convert/output_file.wav"
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        await message.reply(f"```Text output\nOutput:\n{text}```")
    except sr.UnknownValueError:
        await message.reply("I cannot understand the audio!")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        await message.reply(f"Error: {e}")
    await r("rm -rf voice_convert")
