from bot import bot


async def invite_user(chat_id: int):
    await bot.send_message(
        chat_id=chat_id, text=f"Вы получили бонус за приглашение друга!"
    )
