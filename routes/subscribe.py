from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from connector import get_connector

import config

from bot import bot
from data import subscribe, points


async def handler(message: Message):
    chat_id = message.chat.id
    connector = get_connector(chat_id)
    connected = await connector.restore_connection()
    if not connected:
        await message.answer("Подключите кошелёк!")
        return

    text = f"🔗 Подпишитесь на канал, чтобы получить бонус {config.SUBSCRIBE_BONUS} {config.JETTON_SYMBOL}!"
    mk_b = InlineKeyboardBuilder()
    mk_b.row(InlineKeyboardButton(text=f"Подписаться", url=config.CHANNEL_LINK))
    mk_b.row(
        InlineKeyboardButton(
            text="Проверить подписку", callback_data="check_subscribe"
        ),
    )
    await message.answer(text=text, reply_markup=mk_b.as_markup())


async def check(message: Message):
    chat_id = message.chat.id
    status = await subscribe.get(chat_id)
    if status is True:
        await message.answer("✅ Вы уже получили бонус за подписку!")
        return
    member = await bot.get_chat_member(config.CHANNEL_ID, chat_id)
    if (
        member.status == "member"
        or member.status == "creator"
        or member.status == "administrator"
    ):
        await points.add(chat_id, config.SUBSCRIBE_BONUS)
        await message.answer(
            f"🎉 Вы подписаны на канал и получили бонус {config.SUBSCRIBE_BONUS} {config.JETTON_SYMBOL}!"
        )
        await subscribe.set(chat_id)
    else:
        await message.answer("❌ Вы не подписаны на канал!")
