import os
from dotenv import load_dotenv, find_dotenv

# if not find_dotenv():
#     exit("Переменные окружения не загружены т.к отсутствует файл .env")
# else:
#     load_dotenv()

BOT_TOKEN = "5881389387:AAFC2UbytWDG4fAGtXTISko9W3Qq0w0Gctw"
# RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку")
)
