# Powered By Nihal_XD IF You Fresh Any Problem To Contact The Owner

# Powered By @Mr_Nihal9

# ©️ Copy Right By Nihal_XD

# Any Problem To Report @Mr_Nihal9

# Bot Owner @Mr_Nihal9

import asyncio
from datetime import datetime

from Nihal import config
from Nihal import app
from Nihal.core.call import Nihal, autoend
from Nihal.utils.database import (get_client, is_active_chat,
                                       is_autoend)


async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        while not await asyncio.sleep(
            config.AUTO_LEAVE_ASSISTANT_TIME
        ):
            from NihalX.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                try:
                    async for i in client.iter_dialogs():
                        chat_type = i.chat.type
                        if chat_type in [
                            "supergroup",
                            "group",
                            "channel",
                        ]:
                            chat_id = i.chat.id
                            if (
                                chat_id != Nihal.config.LOG_GROUP_ID
                                and chat_id != -1001438979109
                            ):
                                if not await is_active_chat(chat_id):
                                    try:
                                        await client.leave_chat(
                                            chat_id
                                        )
                                    except:
                                        continue
                except:
                    pass


asyncio.create_task(auto_leave())


async def auto_end():
    while not await asyncio.sleep(5):
        if not await is_autoend():
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await Nihal.stop_stream(chat_id)
                except:
                    continue
                try:
                    await app.send_message(
                        chat_id,
                        "🌷 ǫᴜᴇᴇɴ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ ᴀᴜᴛᴏ ʟᴇғᴛ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ 🌷.",
                    )
                except:
                    continue


asyncio.create_task(auto_end())
