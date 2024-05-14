from pytoniq_core import Address

from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from connector import get_connector
from utils.tonapi import jetton_balance
import data

import config


async def handler(message: Message):
    chat_id = message.chat.id
    connector = get_connector(chat_id)
    connected = await connector.restore_connection()
    wallet_address = connector.account.address
    wallet_address = Address(wallet_address).to_str(is_bounceable=False)

    balance = await jetton_balance(wallet_address)
    points = await data.points.get(chat_id)
    invited = await data.referral.get(chat_id)

    text = f"💎 Ваш баланс: {balance} {config.JETTON_SYMBOL}\n"
    text += f"🏦 Доступно к выводу: {points} {config.JETTON_SYMBOL}\n"
    text += f"👥 Приглашено: {invited} человек"

    mk_b = InlineKeyboardBuilder()
    mk_b.row(
        InlineKeyboardButton(text=f"Купить {config.JETTON_SYMBOL}", url=config.BUY_LINK)
    )
    mk_b.row(
        InlineKeyboardButton(text="Пригласить", callback_data="invite"),
        InlineKeyboardButton(text="Бонус за подписку", callback_data="subscribe"),
    )
    mk_b.row(InlineKeyboardButton(text="Отключить кошелёк", callback_data="disconnect"))

    await message.answer(text=text, reply_markup=mk_b.as_markup())
