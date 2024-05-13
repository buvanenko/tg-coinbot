from bot import bot

async def invite_user(chat_id: int):
    await bot.send_message(chat_id, f'Вы получили бонус за приглашение друга!')