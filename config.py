import os

# API CONFIG
API_ID = int(os.environ.get("API_ID", 123456))
API_HASH = os.environ.get("API_HASH", "ABC-DEF1234ghIkl-zyx57W2v1u123ew11")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11")

# REDIS
HOST = os.environ.get("REDIS_HOST", "localhost")
PORT = int(os.environ.get("REDIS_PORT", 6379))
PASSWORD = os.environ.get("REDIS_PASSWORD", "")

PRIVATE_CHAT_ID = int(os.environ.get("PRIVATE_CHAT_ID", -1001234567890))
COOKIE = os.environ.get("COOKIE", "")

# ADMINS
admin_list = os.environ.get("ADMINS", "1317173146")
ADMINS = [int(x) for x in admin_list.split()]

BOT_USERNAME = os.environ.get("BOT_USERNAME", "teraboxdown_bot")
FORCE_LINK = os.environ.get("FORCE_LINK", "@RoldexVerse")
PUBLIC_EARN_API = os.environ.get("PUBLIC_EARN_API", "")
