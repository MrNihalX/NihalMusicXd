# Powered By Nihal_XD 
# ©️ Copy Right By Nihal_XD 
# Any Problem To Report Nihal_XD 
# Bot Owner Nihal_XD 
from pyrogram import filters
from pyrogram.types import Message

from Nihal.config import BANNED_USERS
from Nihal.strings import get_command
from Nihal import app
from Nihal.core.call import Nihal
from Nihal.utils.database import set_loop
from Nihal.utils.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Nihal.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["bh_9"].format(message.from_user.mention)
    )
