import config
from tc_storage import TcStorage

async def add(chat_id: int, count: int = config.INVITE_BONUS):
    storage = TcStorage(chat_id)
    points = await storage.get_item('points')
    if points is None:
        points = points
    else:
        points = int(points) + count
    await storage.set_item('bonus', str(points))

async def get(chat_id: int):
    storage = TcStorage(chat_id)
    invited = await storage.get_item('points')
    return invited if invited else 0