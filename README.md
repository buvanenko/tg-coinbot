# tg-coinbot
![TON](https://img.shields.io/badge/TON-blue) ![Telegram](https://img.shields.io/badge/Telegram-blue) ![Python](https://img.shields.io/badge/Python-blue)
**[WIP]** Telegram бот для TON Jetton. Проверяет наличие указанного в конфиге жеттона, выдает бонусы за подписку на канал и за приглашение друзей.

### Возможности
- Подключение кошельков через TON Connect
- Реферальная система
- Бонусы за подписку

### Установка
Требования: 
- Python 3.12.3
- Redis 6

```sh
git clone https://github.com/buvanenko/tg-coinbot.git
cd tg-coinbot
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

### Запуск

Перед первым запуском сделайте копию файла _example.env_ и переименуйте его в _.env_
Заполните файл _.env_ нужными значениями.
| Имя | Значение |
| ------ | ------ |
| REDIS_HOST | Адрес хоста Redis |
| REDIS_PORT | Порт хоста Redis |
| REDIS_USERNAME | Имя пользователя Redis |
| REDIS_PASSWORD | Пароль пользователя Redis |
| - | - |
| TOKEN | Telegram API токен вашего бота, полученный от [@BotFather](https://t.me/BotFather) |
| BOT_LINK | Ссылка на вашего бота |
| - | - |
| MANIFEST_URL| Ссылка на [TON Connect manifest.json](https://docs.ton.org/develop/dapps/ton-connect/manifest) |
| JETTON | Адрес контракта жеттона |
| JETTON_SYMBOL | Символ жеттона, короткая форма написания |
| BUY_LINK | Ссылка на покупку жеттона |
| - | - |
| CHANNEL_ID | ID Telegram канала, на который нужно подписаться |
| CHANNEL_LINK | Ссылка на Telegram канал, на который нужно подписаться |
| - | - |
| INVITE_BONUS | Бонус за приглашение друга |
| SUBSCRIBE_BONUS | Бонус за подписку на канал |

После создания и заполнения файла .env просто введите команды: 
```sh
. venv/bin/activate
python main.py
```

