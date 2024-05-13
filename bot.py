import config
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

dp = Dispatcher()
bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)