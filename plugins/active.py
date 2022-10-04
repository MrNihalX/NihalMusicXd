# A Powerful Music Bot Property Of Redox Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Redox © @Mr_Nihal9 © REDOXMOD
# Mr Nihal

from pyrogram import filters
from pyrogram.types import Message

from strings import get_command
from Nihal import app
from Nihal.misc import SUDOERS
from Nihal.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)

# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")


@app.on_message(filters.command(ACTIVEVC_COMMAND) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text(
        "💥 ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs 🚴‍♂️\n\n🌷 ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴇᴡ sᴇᴄ..🥀"
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "📌 ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ 🥀"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("🍁 ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴄ ᴏɴ ǫᴜᴇᴇɴ ᴍᴜsɪᴄ ʙᴏᴛ ❎")
    else:
        await mystic.edit_text(
            f"💖 ǫᴜᴇᴇɴ ᴍᴜsɪᴄ ᴄᴜʀʀᴇɴᴛ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ʟɪsᴛ 🔰 :-**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(ACTIVEVIDEO_COMMAND) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text(
        "💥 ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs 🚴‍♂️\n\n🌷 ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴇᴡ sᴇᴄ..🥀"
    )
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "🥀 ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ 🥀"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("🍁 ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴄ ᴏɴ ǫᴜᴇᴇɴ ᴍᴜsɪᴄ ʙᴏᴛ ❎")
    else:
        await mystic.edit_text(
            f"💖 ǫᴜᴇᴇɴ ᴍᴜsɪᴄ ᴄᴜʀʀᴇɴᴛ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ʟɪsᴛ 🔰 :-**\n\n{text}",
            disable_web_page_preview=True,
        )
