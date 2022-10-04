from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from Nihal import app
from Nihal.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Chat"
        logger_text = f"""
**🔰 𝐒𝐡𝐢𝐳𝐮𝐤𝐚_𝐍𝐨𝐛𝐢 𝐏𝐥𝐚𝐲𝐞𝐫 𝐋𝐨𝐠𝐬 🥀**

**🔰 𝐂𝐡𝐚𝐭 𝐍𝐚𝐦𝐞 :** {message.chat.title} [`{message.chat.id}`]

**🥀 𝐔𝐬𝐞𝐫 :** {message.from_user.mention}

**⚜️ 𝐔𝐬𝐞𝐫 𝐍𝐚𝐦𝐞 :** @{message.from_user.username}

**🆔 𝐈𝐝 :** `{message.from_user.id}`

**⚜️ 𝐂𝐡𝐚𝐭 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞 :** {chatusername}

**🥀 𝐏𝐥𝐚𝐲𝐞𝐝 𝐐𝐮𝐚𝐫𝐞𝐲 :** `{message.text}`

**📡 𝐒𝐭𝐫𝐞𝐚𝐦 𝐓𝐲𝐩𝐞 :** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
