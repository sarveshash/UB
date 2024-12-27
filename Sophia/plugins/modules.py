from subprocess import getoutput as r
from pyrogram import Client
from Sophia import *
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

a = r("ls Sophia/plugins").split('\n')
help_data = {}
help_names = []
for x in a:
    if x.endswith('.py') and not x.startswith('__pycache__'):
        try:
            module = __import__(f"Sophia.plugins.{x.replace('.py', '')}", fromlist=["MOD_NAME", "MOD_HELP"])
            if hasattr(module, 'MOD_NAME') and hasattr(module, 'MOD_HELP'):
                help_data[module.MOD_NAME] = module.MOD_HELP
                help_names.append(module.MOD_NAME)
        except:
            pass
logging.info(f"{f'Loaded Modules: {help_names}' if help_names else 'No modules loaded'}")

@SophiaBot.on_inline_query(qfilter('help'))
async def showcommands(_, query):
    buttons = []
    row = []
    for i, cmd in enumerate(help_names):
        row.append(InlineKeyboardButton(cmd, callback_data=f"help: {cmd}"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    reply_markup = InlineKeyboardMarkup(buttons)
    result = InlineQueryResultArticle(
        title="Help",
        input_message_content=InputTextMessageContent("**Here are the available commands:**"),
        reply_markup=reply_markup
    )

    await query.answer([result])

@SophiaBot.on_callback_query(qfilter('help: '))
async def showhelpinfo(_, query):
    help_cmd = str(query.data).replace('help: ', '')
    if help_cmd in help_names:
        txt = f"**⚡ Help for the module: {help_cmd}:**\n\n{help_data[help_cmd]}"
        button = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="helpback")]])
        await query.edit_message_text(txt, reply_markup=button)
        
@SophiaBot.on_callback_query(qfilter('helpback'))
async def backhelp(_, query):
    buttons = []
    row = []
    for i, cmd in enumerate(help_names):
        row.append(InlineKeyboardButton(cmd, callback_data=f"help: {cmd}"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.edit_message_text("**Here are the available commands:**", reply_markup=reply_markup)
