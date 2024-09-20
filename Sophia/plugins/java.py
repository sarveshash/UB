from Sophia import HANDLER
from Sophia import Sophia
from pyrogram import filters
from subprocess import getoutput as run
import asyncio
import os
import io

@Sophia.on_message(filters.command(["java", "je"], prefixes=HANDLER) & filters.user('me'))
async def run_java(_, message):
    if len(message.command) < 2:
        return await message.edit("Please enter a Java command to run! 🥀 ✨")
    
    java_code = message.text.split(None, 1)[1]
    message_text = await message.reply_text("Processing...")
    
    # Write the Java code to a file
    with open("MyProgram.java", "w") as java_file:
        java_file.write(java_code)
    
    # Compile the Java code
    compile_output = run("javac MyProgram.java")
    
    if compile_output:
        await message_text.edit(f"Compilation Error:\n{compile_output}")
        return
    # Run the compiled Java program
    output = run("java MyProgram")
    
    # Clean up: remove the Java files
    os.remove("MyProgram.java")
    os.remove("MyProgram.class")
    oo = message.text
    await message.edit(f"```java\n{oo}```")
    if len(output) > 4096:
        with io.BytesIO(str.encode(output)) as out_file:
            out_file.name = "java_output.txt"
            await message.reply_document(
                document=out_file, disable_notification=True
            )
            await message_text.delete()
    else:
        await message_text.edit(f"Output:\n```Output\n{output}```")
