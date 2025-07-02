from keep_alive import keep_alive
import asyncio
import logging
from telethon import TelegramClient, events

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Start keep_alive server
keep_alive()

# Telegram credentials (use environment variables in Render)
import os
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
session_name = "bot"

# Source and destination
from_chat = -1001563681038  # Replace with source chat ID
to_chat = "https://t.me/Human_toss_line"

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=from_chat))
async def handler(event):
    await client.send_message(to_chat, event.message)

async def main():
    await client.start()
    logger.info("Bot is running...")
    await client.run_until_disconnected()

# Start event loop directly
asyncio.get_event_loop().run_until_complete(main() 
