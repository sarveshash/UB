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
logging.info(f"{f'Loaded Modules: {a}' if a else 'No modules loaded'}")

async def paginate_help(page=1, per_page=4):
    start = (page - 1) * per_page
    end = start + per_page
    buttons = []
    row = []
    for cmd in help_names[start:end]:
        row.append(InlineKeyboardButton(cmd, callback_data=f"help: {cmd}"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    nav_buttons = []
    if page > 1:
        nav_buttons.append(InlineKeyboardButton("🔙 Back", callback_data=f"helppage:{page - 1}"))
    if end < len(help_names):
        nav_buttons.append(InlineKeyboardButton("Next 🔜", callback_data=f"helppage:{page + 1}"))
    if nav_buttons:
        buttons.append(nav_buttons)
    return InlineKeyboardMarkup(buttons)

@SophiaBot.on_inline_query(qfilter('help'))
async def showcommands(_, query):
    reply_markup = await paginate_help(page=1)
    result = InlineQueryResultArticle(
        title="Help",
        input_message_content=InputTextMessageContent("**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**"),
        reply_markup=reply_markup
    )
    await query.answer([result])

@SophiaBot.on_callback_query(qfilter('help: '))
async def showhelpinfo(_, query):
    help_cmd = str(query.data).replace('help: ', '')
    if help_cmd in help_names:
        txt = f"**⚡ Help for the module: {help_cmd}**\n\n{help_data[help_cmd]}"
        current_page = (help_names.index(help_cmd) // 10) + 1
        button = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data=f"helppage:{current_page}")]])
        await query.edit_message_text(txt, reply_markup=button)

@SophiaBot.on_callback_query(qfilter('helppage:'))
async def page_callback(_, query):
    page = int(query.data.split(":")[1])
    reply_markup = await paginate_help(page=page)
    await query.edit_message_text("**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**", reply_markup=reply_markup)
