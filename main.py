# main.py

import sys
import logging
import asyncio

from pytoniq_core import Address
from pytonconnect import TonConnect

from connector import get_connector

from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot import bot, dp
import routes
import data


logger = logging.getLogger(__file__)


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    if " " in message.text:
        refferal = int(message.text.split(" ")[1])
        print(refferal)
        await data.referral.save(message.chat.id, refferal)

    chat_id = message.chat.id
    connector = get_connector(chat_id)
    connected = await connector.restore_connection()

    mk_b = InlineKeyboardBuilder()
    if connected:
        await routes.wallet.handler(message)
    else:
        wallets_list = TonConnect.get_wallets()
        for wallet in wallets_list:
            mk_b.button(text=wallet['name'], callback_data=f'connect:{wallet["name"]}')
        mk_b.adjust(1, )
        await message.answer(text='Выберите кошелёк для подключения:', reply_markup=mk_b.as_markup())



async def connect_wallet(message: Message, wallet_name: str):
    connector = get_connector(message.chat.id)

    wallets_list = connector.get_wallets()
    wallet = None

    for w in wallets_list:
        if w['name'] == wallet_name:
            wallet = w

    if wallet is None:
        raise Exception(f'Unknown wallet: {wallet_name}')

    generated_url = await connector.connect(wallet)

    mk_b = InlineKeyboardBuilder()
    mk_b.button(text='Подключить', url=generated_url)

    await message.answer(text='Подключите кошелёк в течение 3 минут', reply_markup=mk_b.as_markup())

    mk_b = InlineKeyboardBuilder()
    mk_b.button(text='Старт', callback_data='start')

    for i in range(1, 180):
        await asyncio.sleep(1)
        if connector.connected:
            if connector.account.address:
                wallet_address = connector.account.address
                wallet_address = Address(wallet_address).to_str(is_bounceable=False)
                await message.answer(f'Вы подключены с адресом <code>{wallet_address}</code>', reply_markup=mk_b.as_markup())
                logger.info(f'Connected with address: {wallet_address}')
            return

    await message.answer(f'Время подключения истекло!', reply_markup=mk_b.as_markup())


async def disconnect_wallet(message: Message):
    connector = get_connector(message.chat.id)
    await connector.restore_connection()
    await connector.disconnect()
    await message.answer('Вы были успешно отключены!')


@dp.callback_query(lambda call: True)
async def main_callback_handler(call: CallbackQuery):
    await call.answer()
    message = call.message
    data = call.data
    if data == "start":
        await command_start_handler(message)
    elif data == 'disconnect':
        await disconnect_wallet(message)
    elif data == 'invite':
        await routes.refferal.handler(message)
    else:
        data = data.split(':')
        if data[0] == 'connect':
            await connect_wallet(message, data[1])


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)  # skip_updates = True
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
