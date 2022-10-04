# A Powerful Music Bot Property Of Redox Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Redox © @Mr_Nihal9 © REDOXMOD
# Mr Nihal


from typing import Dict, List, Union

from Nobita.core.mongo import mongodb


onoffdb = mongodb.onoffper


async def is_on_off(on_off: int) -> bool:
    onoff = await onoffdb.find_one({"on_off": on_off})
    if not onoff:
        return False
    return True


async def add_on(on_off: int):
    is_on = await is_on_off(on_off)
    if is_on:
        return
    return await onoffdb.insert_one({"on_off": on_off})


async def add_off(on_off: int):
    is_off = await is_on_off(on_off)
    if not is_off:
        return
    return await onoffdb.delete_one({"on_off": on_off})
