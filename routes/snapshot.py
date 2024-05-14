from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command


import data
import config

router = Router()


@router.message(Command("snapshot"))
async def handler(message: Message):
    chat_id = message.chat.id
    if chat_id not in config.BOT_ADMINS:
        return

    await data.snapshot.save()
    # отправляем файл snapshot.csv
    await message.answer_document(FSInputFile("snapshot.csv"))
