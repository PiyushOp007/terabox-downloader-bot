import os
from flask import Flask
import threading
import asyncio
from config import BOT_TOKEN
from bot_client import bot

# Import to register handlers
import main
import bot as bot_handlers

app = Flask(__name__)

@app.route("/")
def index():
    return "I'm alive"

def run_bot():
    try:
        print("Starting Telegram Bot...")
        bot.start(bot_token=BOT_TOKEN)
        bot.run_until_disconnected()
    except Exception as e:
        print(f"Error running bot: {e}")

# Start bot in a separate thread
threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
