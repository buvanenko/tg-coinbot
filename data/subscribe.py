
from tc_storage import TcStorage

async def set(chat_id: int):
    storage = TcStorage(chat_id)
    await storage.set_item('subscribe', str(True))

async def get(chat_id: int):
    storage = TcStorage(chat_id)
    subscribe = await storage.get_item('subscribe')
    return True if subscribe else False