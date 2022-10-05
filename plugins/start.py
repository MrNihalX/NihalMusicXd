# Powered By  Nihal_XD 
# ©️ Copy Right By Nihal_XD 
# Any Problem To Report Nihal_XD 
# Bot Owner Nihal_XD 

import asyncio

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from Nihal import app
from Nihal import config
from Nihal.config import BANNED_USERS
from Nihal.config.config import OWNER_ID
from Nihal.strings import get_command, get_string
from Nihal import Telegram, YouTube, app
from Nihal.misc import SUDOERS
from plugins.playlist import del_plist_msg
from plugins.sudoers import sudoers_list
from Nihal.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from Nihal.utils.decorators.language import LanguageStart
from Nihal.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

loop = asyncio.get_running_loop()


@app.on_message(
    filters.command(["start"])
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_text(
                _["help_1"], reply_markup=keyboard
            )
        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])
        if name[0:3] == "sta":
            m = await message.reply_text(
                "🔎 ғᴇᴛᴄʜɪɴɢ ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ sᴛᴀᴛs 📊.!"
            )
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"🛡️[ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ 🍁](https://t.me/telegram) **🔊 ᴘʟᴀʏᴇᴅ {count} ⏱️ ᴛɪᴍᴇs**\n\n"
                    else:
                        msg += f"🛡️ [{title}](https://www.youtube.com/watch?v={vidid}) **🔊 ᴘʟᴀʏᴇᴅ {count} ⏱️ ᴛɪᴍᴇs**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(
                    None, get_stats
                )
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ʜᴀs ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ǫᴜᴇᴇɴ ʙᴏᴛ ᴄʜᴇᴄᴋ  <code>SUDOLIST</code>\n\n**🆔 ᴜsᴇʀ ɪᴅ:** {sender_id}\n**👑 ᴜsᴇʀ ɴᴀᴍᴇ:** {sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                return await Telegram.send_split_text(message, lyrics)
            else:
                return await message.reply_text(
                    "⚜️ ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇᴛ ʟʏʀɪᴄs ❌."
                )
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name[0:3] == "inf":
            m = await message.reply_text("🔎 sᴇᴀʀᴄʜɪɴɢ Info!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[
                    0
                ]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
__**🌷 ǫᴜᴇᴇɴ ᴠɪᴅᴇᴏ ᴛʀᴀᴄᴋᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ 🌷**__
                        
                ❰ ǫᴜᴇᴇɴ ⚜️ ᴘʟᴀʏᴇʀ ❱
                        
📌**ᴛɪᴛᴀʟ:** {title}

⏱️**ᴅᴜʀᴀᴛɪᴏɴ:** {duration} Mins
👀**ᴠɪᴇᴡs:** `{views}`
⏰**ᴘᴜʙʟɪsʜᴇᴅ ᴛɪᴍᴇ:** {published}
📡**ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ:** {channel}
📡 **ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ:** [👀 ᴠɪᴇᴡ ᴄʜᴀɴɴᴇʟ 📡]({channellink})
🛡️ **ᴠɪᴅᴇᴏ ʟɪɴᴋ:** [📎 ʟɪɴᴋ 📎]({link})

🔍️ sᴇᴀʀᴄʜᴇᴅ ᴘᴏᴡᴇʀᴇᴅ ʙʏ 🌷 {Nihal.config.MUSIC_BOT_NAME}__"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🌷 ᴡᴀᴛᴄʜ 📺", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="❌ ᴄʟᴏsᴇ ❌", callback_data="close"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
            if await is_on_off(Nihal.config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    Nihal.config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴍᴜsɪᴄ ʙᴏᴛ 🎵  ᴛᴏ ᴄʜᴇᴄᴋ <code>🥀 ᴠɪᴅᴇᴏ ɪɴғᴏʀᴍᴀᴛɪᴏɴ </code>\n\n**🆔 ᴜsᴇʀ ɪᴅ:** {sender_id}\n**👑 ᴜsᴇʀ ɴᴀᴍᴇ:** {sender_name}",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        out = private_panel(_, app.username, OWNER)
        if config.START_IMG_URL:
            try:
                await message.reply_photo(
        photo=f"https://telegra.ph/file/c109030256a4526907118.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
🎧 ʜᴇʏ, ɪ ᴀᴍ ǫᴜᴇᴇɴ ʙᴏᴛ sᴜᴘᴇʀғᴀsᴛ ʜɪɢʜ ϙᴜᴀʟɪᴛʏ
ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ᴏᴜʀ ɢʀᴏᴜᴘ ғᴏʀ ᴘʟᴀʏɪɴɢ ᴀ sᴏɴɢ.

┏━━━━━━━━━━━━━━━━━┓
┣★ ᴏᴡɴᴇʀ xᴅ : [ɴɪʜᴀʟ_xᴅ](https://t.me/Mr_Nihal9)
┣★ ʙᴏᴛ ɴᴀᴍᴇ  : [ɴɪʜᴀʟ_ᴍᴜsɪᴄ](https://t.me/CuteQueenBot)
┣★ ᴜᴘᴅᴀᴛᴇs » : [ɴɪʜᴀʟ_ʟᴏɢᴏ](https://t.me/Redoxmod)
┣★ sᴜᴘᴘᴏʀᴛ » : [ᴀʙᴏᴜᴛ_ɴɪʜᴀʟ](https://t.me/AboutNihal)
┣★ ᴄʜᴀᴛ  » : [ɴɪʜᴀʟ_ᴄʜᴀᴛ](https://t.me/Mr_Nihal9)
┗━━━━━━━━━━━━━━━━━┛

🌺 ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ » ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ 
ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴡɪᴛʜ ʜɪɢʜ ϙᴜᴀʟɪᴛʏ ❥︎ᴍᴜsɪᴄ.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎧 ❰ ᴜᴛʜᴀᴀʟᴇ ʀᴇ ʙᴀʙᴀ ❱ 🎧", url=f"https://t.me/{app.username}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(
                        "🌺 ❰ ɴɪʜᴀʟ_ʟᴏɢᴏ ❱ 🌺", url=f"https://t.me/Redoxmod"),
                ],
                [
                    InlineKeyboardButton(
                        text="⚙️ ❰ ᴄᴏᴍᴍᴀɴᴅs ❱ ⚙️", callback_data="settings_back_helper")
                ]
           ]
        ),
                  )
            except:
                await message.reply_photo(
        photo=f"https://telegra.ph/file/c109030256a4526907118.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
🎧 ʜᴇʏ, ɪ ᴀᴍ ǫᴜᴇᴇɴ ʙᴏᴛ sᴜᴘᴇʀғᴀsᴛ ʜɪɢʜ ϙᴜᴀʟɪᴛʏ
ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ᴏᴜʀ ɢʀᴏᴜᴘ ғᴏʀ ᴘʟᴀʏɪɴɢ ᴀ sᴏɴɢ.

┏━━━━━━━━━━━━━━━━━┓
┣★ ᴏᴡɴᴇʀ xᴅ : [ɴɪʜᴀʟ_xᴅ](https://t.me/Mr_Nihal9)
┣★ ʙᴏᴛ ɴᴀᴍᴇ  : [ɴɪʜᴀʟ_ᴍᴜsɪᴄ](https://t.me/CuteQueenBot)
┣★ ᴜᴘᴅᴀᴛᴇs » : [ɴɪʜᴀʟ_ʟᴏɢᴏ](https://t.me/Redoxmod) 
┣★ sᴜᴘᴘᴏʀᴛ » : [ᴀʙᴏᴜᴛ_ɴɪʜᴀʟ](https://t.me/AboutNihal) 
┣★ ᴄʜᴀᴛ  » : [ɴɪʜᴀʟ_ᴄʜᴀᴛ](https://t.me/Mr_Nihal9) 
┗━━━━━━━━━━━━━━━━━┛

🌺 ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ » ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ 
ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴡɪᴛʜ ʜɪɢʜ ϙᴜᴀʟɪᴛʏ ❥︎ᴍᴜsɪᴄ.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎧 ❰ ᴜᴛʜᴀᴀʟᴇ ʀᴇ ʙᴀʙᴀ ❱ 🎧", url=f"https://t.me/{app.username}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(
                        "🌺 ❰ ɴɪʜᴀʟ_ʟᴏɢᴏ ❱ 🌺", url=f"https://t.me/Redoxmod"),
                ],
                [
                    InlineKeyboardButton(
                        text="⚙ ❰ ᴄᴏᴍᴍᴀɴᴅs ❱ ⚙", callback_data="settings_back_helper")
                ]
           ]
        ),
              )
        else:
            await message.reply_photo(
        photo=f"https://telegra.ph/file/c109030256a4526907118.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
🎧  ʜᴇʏ, ɪ ᴀᴍ ǫᴜᴇᴇɴ ʙᴏᴛ sᴜᴘᴇʀғᴀsᴛ ʜɪɢʜ ϙᴜᴀʟɪᴛʏ
ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ᴏᴜʀ ɢʀᴏᴜᴘ ғᴏʀ ᴘʟᴀʏɪɴɢ ᴀ sᴏɴɢ.

┏━━━━━━━━━━━━━━━━━┓
┣★ ᴏᴡɴᴇʀ xᴅ : [ɴɪʜᴀʟ_xᴅ](https://t.me/Mr_Nihal9)
┣★ ʙᴏᴛ ɴᴀᴍᴇ  : [ɴɪʜᴀʟ_ᴍᴜsɪᴄ](https://t.me/CuteQueenBot)
┣★ ᴜᴘᴅᴀᴛᴇs » : [ɴɪʜᴀʟ_ʟᴏɢᴏ](https://t.me/Redoxmod) 
┣★ sᴜᴘᴘᴏʀᴛ » : [ᴀʙᴏᴜᴛ_ɴɪʜᴀʟ](https://t.me/AboutNihal) 
┣★ ᴄʜᴀᴛ  » : [ɴɪʜᴀʟ_ᴄʜᴀᴛ](https://t.me/Mr_Nihal9)
┗━━━━━━━━━━━━━━━━━┛

🌺 ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ » ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ 
ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴡɪᴛʜ ʜɪɢʜ ϙᴜᴀʟɪᴛʏ ❥︎ᴍᴜsɪᴄ.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎧 ❰ ᴜᴛʜᴀᴀʟᴇ ʀᴇ ʙᴀʙᴀ ❱ 🎧", url=f"https://t.me/{app.username}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(
                        "🌺 ❰ ɴɪʜᴀʟ_ʟᴏɢᴏ ❱ 🌺", url=f"https://t.me/Redoxmod"),
                ],
                [
                    InlineKeyboardButton(
                        text="⚙ ❰ ᴄᴏᴍᴍᴀɴᴅs ❱ ⚙", callback_data="settings_back_helper")
                ]
           ]
        ),
           )
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} ʜᴀs ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ǫᴜᴇᴇɴ ʙᴏᴛ 🌷.\n\n**🆔 ᴜsᴇʀ ɪᴅ:** {sender_id}\n**👑 ᴜsᴇʀɴᴀᴍᴇ:** {sender_name}",
            )


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def testbot(client, message: Message, _):
    out = start_pannel(_)
    return await message.reply_text(
        "**✅ ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴍᴇ ɪɴ\nᴄʜᴀᴛ »  {0}\n\n🥀 ɪғ ʜᴀᴠᴇ 📀 ᴀɴʏ ϙᴜᴇʀɪᴇs\nᴛʜᴇɴ ᴇxᴘʟᴀɪɴ 💬 ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ 👑.\n\n💐 ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ‖ sᴜᴘᴘᴏʀᴛ 🌷\n🌷 ғᴏʀ ɢᴇᴛᴛɪɴɢ ɴᴇᴡ ᴜᴘᴅᴀᴛᴇs 💞...**".format(
            message.chat.title, Nihal.config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )


welcome_group = 2


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**🔒ᴘʀɪᴠᴀᴛᴇ ᴍᴜsɪᴄ ʙᴏᴛ 🎵**\n\n💰ᴏɴʟʏ ғᴏʀ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴄʜᴀᴛs ғʀᴏᴍ ᴛʜᴇ ᴏᴡɴᴇʀ 👑. ᴀsᴋ ᴍʏ ᴏᴡɴᴇʀ ᴛᴏ ᴀʟʟᴏᴡ ʏᴏᴜʀ ᴄʜᴀᴛ ғɪʀsᴛ 🌷."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != "supergroup":
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                out = start_pannel(_)
                await message.reply_text(
                    _["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in Nihal.config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            return
        except:
            return
