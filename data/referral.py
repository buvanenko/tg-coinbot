from tc_storage import TcStorage

from data import points
from events import invite

async def save(chat_id: int, inviter: int):
    # добавлем приглашенному инфу о пригласившем
    storage = TcStorage(chat_id)
    inviter = await storage.get_item('inviter')
    if inviter:
        return
    await storage.set_item('inviter', str(inviter))

    # добавляем пригласившему инфу о приглашенном
    storage = TcStorage(inviter)
    
    invited = await storage.get_item('invited')
    if invited is None:
        invited = 1
    else :
        invited = int(invited) + 1
    await storage.set_item('invited', str(invited))

    # начисляем бонус
    await points.add(inviter)
    await invite.invite_user(inviter)

async def get(chat_id: int):
    storage = TcStorage(chat_id)
    invited = await storage.get_item('invited')
    return invited if invited else 0