MAX_GPT_TOKENS = 100  # Максимальный количество символов для текстового ответа бота
MAX_USER_STT_BLOCKS = 12  # Максимальное количество аудиоблоков
MAX_USER_TTS_SYMBOLS = 1000  # Максимальное количество символов всех голосовых ответов для пользователя
MAX_USER_GPT_TOKENS = 1200  # Максимальное количество токенов текствых ответов для пользователя
MAX_TTS_SYMBOLS = 300  # Максимальное количество символов голосовых ответов для пользователя
COUNT_LAST_MSG = 3  # Количество сохраняемых сообщений от пользователя в БД


HOME_DIR = '/home/student/final_project'  # путь к папке с проектом
LOGS = 'logs.txt'  # файл для логов
DB_FILE = 'messages.db'  # файл для базы данных

SYSTEM_PROMPT = [{'role': 'system', 'text': """Ты GPT-модель, которая должна отвечать на все вопросы пользователя.
                                               Будь вежливым"""}]  # как будет отвечать GPT(СИСТЕМНЫЙ ПРОМПТ)