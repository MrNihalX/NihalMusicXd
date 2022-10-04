# Powered By Nihal_XD IF You Fresh Any Problem To Contact The Owner

# Powered By @Mr_Nihal9

# ©️ Copy Right By Nihal_XD

# Any Problem To Report @Mr_Nihal9

# Bot Owner @Mr_Nihal9

from pyrogram import filters

from Nihal import config
from Nihal.strings import get_command
from Nihal import app
from Nihal.misc import SUDOERS
from Nihal.utils.database import autoend_off, autoend_on
from Nihal.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "🔰 ᴜsᴀɢᴇ 🔰 :\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "🔰 ᴀᴜᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍ ᴇɴᴀʙʟᴇᴅ ✅.\n\n💥 ǫᴜᴇᴇɴ ᴍᴜsɪᴄ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ ᴡɪʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴡʜᴇɴ ᴀɴʏᴏɴᴇ ɴᴏ ᴀᴄᴛɪᴠᴇ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀɴᴅ ʙᴏᴛ sᴇɴᴅ ᴀ ʟᴇᴀᴠᴇ ᴍᴀssᴀɢᴇ 📝."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("🔰 ᴀᴜᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍ ᴅɪsᴀʙʟᴇᴅ ❎.")
    else:
        await message.reply_text(usage)
