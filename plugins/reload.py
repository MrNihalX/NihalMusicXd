# Powered By Nihal_XD 
# ©️ Copy Right By Nihal_XD 
# Any Problem To Report Nihal_XD 
# Bot Owner Nihal_XD 

import asyncio

from pyrogram import filters
from pyrogram.types import CallbackQuery, Message

from Nihal.config import BANNED_USERS, MUSIC_BOT_NAME, adminlist, lyrical
from Nihal.strings import get_command
from Nihal import app
from Nihal.core.call import Nihal 
from Nihal.misc import db
from Nihal.utils.database import get_authuser_names, get_cmode
from Nihal.utils.decorators import (ActualAdminCB, AdminActual,
                                         language)
from Nihal.utils.formatters import alpha_to_int

### Multi-Lang Commands
RELOAD_COMMAND = get_command("RELOAD_COMMAND")
RESTART_COMMAND = get_command("RESTART_COMMAND")


@app.on_message(
    filters.command(RELOAD_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def reload_admin_cache(client, message: Message, _):
    try:
        chat_id = message.chat.id
        admins = await app.get_chat_members(
            chat_id, filter="administrators"
        )
        authusers = await get_authuser_names(chat_id)
        adminlist[chat_id] = []
        for user in admins:
            if user.can_manage_voice_chats:
                adminlist[chat_id].append(user.user.id)
        for user in authusers:
            user_id = await alpha_to_int(user)
            adminlist[chat_id].append(user_id)
        await message.reply_text(_["admin_20"])
    except:
        await message.reply_text(
            "🌷ᴀᴅᴍɪɴ ʟɪsᴛ ʀᴇғʀᴇsʜ ғᴀɪʟᴇᴅ ❌, ᴍᴀᴋᴇ sᴜʀᴜ ʏᴏᴜ ᴘʀᴏᴍᴏᴛᴇᴅ ᴛʜᴇ sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ᴍᴜsɪᴄ ʙᴏᴛ ✅."
        )


@app.on_message(
    filters.command(RESTART_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminActual
async def restartbot(client, message: Message, _):
    mystic = await message.reply_text(
        f"🌷 ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴇᴡ ᴍɪɴ ,{MUSIC_BOT_NAME} ɪs ʀᴇsᴛᴀʀᴛɪɴɢ ɪɴ ᴛʜɪs ᴄʜᴀᴛ ♻️."
    )
    await asyncio.sleep(1)
    try:
        db[message.chat.id] = []
        await Bikashh.stop_stream(message.chat.id)
    except:
        pass
    chat_id = await get_cmode(message.chat.id)
    if chat_id:
        try:
            await app.get_chat(chat_id)
        except:
            pass
        try:
            db[chat_id] = []
            await Bikashh.stop_stream(chat_id)
        except:
            pass
    return await mystic.edit_text(
        f"🌷sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴛᴀʀᴛᴇᴅ ✅ {MUSIC_BOT_NAME} ɪs ʏᴏᴜʀ ᴄʜᴀᴛ, 🌸 ɴᴏᴡ sᴛᴀʀᴛᴇᴅ ʙᴏᴛ ᴀɢᴀɪɴ & ᴘʟᴀʏɪɴɢ ᴀɢᴀɪɴ ✅..."
    )


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(
    filters.regex("stop_downloading") & ~BANNED_USERS
)
@ActualAdminCB
async def stop_download(client, CallbackQuery: CallbackQuery, _):
    message_id = CallbackQuery.message.message_id
    task = lyrical.get(message_id)
    if not task:
        return await CallbackQuery.answer(
            "🌷 ᴅᴏᴡɴʟᴏᴀᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴏɴᴇ ✅.", show_alert=True
        )
    if task.done() or task.cancelled():
        return await CallbackQuery.answer(
            "🌷 ᴅᴏᴡɴʟᴏᴀᴅ ᴀʟʀᴇᴀᴅʏ ᴅᴏɴᴇ ✅  & ᴄᴀɴᴄʟᴇ ❌.",
            show_alert=True,
        )
    if not task.done():
        try:
            task.cancel()
            try:
                lyrical.pop(message_id)
            except:
                pass
            await CallbackQuery.answer(
                "🔰 ᴅᴏᴡɴʟᴏᴀᴅ ᴄʟᴏsᴇ  ❌.", show_alert=True
            )
            return await CallbackQuery.edit_message_text(
                f"📌 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴄʟᴏsᴇ ʙʏ {CallbackQuery.from_user.mention} ❌"
            )
        except:
            return await CallbackQuery.answer(
                "🌷 ᴅᴏᴡɴʟᴏᴀᴅ ᴄʟᴏsᴇ ғᴀɪʟᴅ ❌ ᴄʟᴏsᴇ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...", show_alert=True
            )
    await CallbackQuery.answer(
        "🌷 ғᴀɪʟᴅ ᴛᴏ ʀᴇᴄᴏɢɴɪᴢᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴛᴀsᴋ 📌.", show_alert=True
    )
