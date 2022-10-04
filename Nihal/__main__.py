# A Powerful Music Bot Property Of Redox Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Redox © @Mr_Nihal9 © REDOXMOD
# Mr Nihal

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Nihal import LOGGER, app, userbot
from Nihal.core.call import Nihal
from Nihal.plugins import ALL_MODULES
from Nihal.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Nihal").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Nihal").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Nihal.plugins" + all_module)
    LOGGER("Nihal.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Nihal.start()
    try:
        await Nihal.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Nihal").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Nihal.decorators()
    LOGGER("Nihal").info("ǫᴜᴇᴇɴ ᴍᴜsɪᴄ Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Nihal").info("Stopping ǫᴜᴇᴇɴ ᴍᴜsɪᴄ Bot! GoodBye")
