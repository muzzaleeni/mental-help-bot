import os
from dotenv import load_dotenv, find_dotenv

# Loading .env variables
load_dotenv(find_dotenv())

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    raise Exception("Please setup the .env variable TELEGRAM_TOKEN.")

PORT = int(os.environ.get('PORT', '8443'))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")

TELEGRAM_SUPPORT_CHAT_ID = os.getenv("TELEGRAM_SUPPORT_CHAT_ID")
if TELEGRAM_SUPPORT_CHAT_ID is None or not str(TELEGRAM_SUPPORT_CHAT_ID).lstrip("-").isdigit():
    raise Exception("You need to specify 'TELEGRAM_SUPPORT_CHAT_ID' env variable: The bot will forward all messages to this chat_id. Add this bot https://t.me/ShowJsonBot to your private chat to find its chat_id.")
TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)


WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE", '''
Привет!

Этот бот представляет ученикам Атырауского лицея "Білім-Инновация" возможность анонимно рассказать о душевных переживаниях, поделиться проблемами и поговорить на тревожные вам темы с нашим школьным психологом, Ришат беем. Чтобы ваш запрос был принят всего лишь напишите о своей проблеме в удобной вам форме.

Просим вас не засорять бота сообщениями не относящимися к его теме, это помешает его работе и соответственно ученикам лицея.
Мы гарантируем вам анонимность и быстрый отклик на ваши сообщения.
''')
REPLY_TO_THIS_MESSAGE = os.getenv("REPLY_TO_THIS_MESSAGE", "Пользователь выше не разрешает пересылать свои сообщения. Ответьте на это сообщение.")
WRONG_REPLY = os.getenv("WRONG_REPLY", "Вы должны ответить на ответ бота под перенаправленным пользователем сообщением.")