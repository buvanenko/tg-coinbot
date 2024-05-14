from aiogram.types import Message

from connector import get_connector

import config


async def handler(message: Message):
    chat_id = message.chat.id
    connector = get_connector(chat_id)
    connected = await connector.restore_connection()
    if not connected:
        await message.answer("Подключите кошелёк!")
        return

    link = config.BOT_LINK + f"?start={chat_id}"

    text = f"🔗 Ваша реферальная ссылка:\n {link}\n\nПолучите {config.INVITE_BONUS} {config.JETTON_SYMBOL} за каждого пришлашенного друга!"

    await message.answer(text=text)
