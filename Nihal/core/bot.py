# Powered By Nihal_XD IF You Fresh Any Problem To Contact The Owner

import sys
from pyrogram import Client
import config
from ..logging import LOGGER



class NihalXBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            "Queen bot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "**😍 ǫᴜᴇᴇɴ ᴍᴜsɪᴄ ʙᴏᴛ ɪs sᴛᴀʀᴛᴇᴅ ᴛᴏ ᴘʟᴀʏ ᴀɴʏ ᴛʜɪɴɢ 🎧**"
            )
        except:
            LOGGER(__name__).error(
                "🎧 ʙᴏᴛ ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ʟᴏɢ ɢʀᴏᴜᴘ . 📌 ᴍᴀᴋᴇ sᴜʀᴜ ʏᴏᴜ ᴀᴅᴅ ᴛʜᴇ ʟᴏɢ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀs ᴀᴅᴍɪɴ  "
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "🎧 ᴘʟᴇᴀsᴇ ᴘʀᴏᴍᴏᴛᴇ ᴍᴜsɪᴄ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ʟᴏɢɢᴇʀ ɢʀᴏᴜᴘ  👑"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"🎧 ǫᴜᴇᴇɴ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ ᴀs {self.name}")
