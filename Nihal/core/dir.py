# Powered By Nihal_XD IF You Fresh Any Problem To Contact The Owner

import os
import sys
from os import listdir, mkdir

from ..logging import LOGGER


def dirr():
    if "resource" not in listdir():
        LOGGER(__name__).warning(
            f"📌 ᴀssᴇᴛs ғᴏʟᴅᴇʀ ɴᴏᴛ ғᴏᴜɴᴅ ❌.\n\n 🥀 ᴘʟᴇᴀsᴇ ᴄʟᴏɴᴇ ʀᴇᴘᴏ ᴀɢᴀɪɴ  🌺."
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("Directories Updated.")
