from aiogram.types import Message

import data
import config

async def handler(message: Message):
    chat_id = message.chat.id
    if chat_id not in config.BOT_ADMINS:
        return
    
    stats = await data.stats.get()
    text = f"Подключений: {stats.connections}\nПодписок: {stats.subscribes}\nБаллов: {stats.points}\nПриглашений: {stats.invited}"
    await message.answer(text)