import logging
from telethon.sync import TelegramClient
from config import API_ID, API_HASH

# Configure logging
logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO
)

# Initialize the client
# We use a single session name 'bot_session' to share the session for both main and bot functionalities
# or we can keep 'bot' as the session name used in bot.py
bot = TelegramClient("bot_session", API_ID, API_HASH)
