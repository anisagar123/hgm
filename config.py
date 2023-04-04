import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5800078311:AAFeq-7UDwnq8KiZEJOa-YHT228jgYRMCk4")
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "bb8f36f9c39a24c7f8b2acbc7ea8c60a")
    DB_URL = os.environ.get("DATABASE_URL", "")
