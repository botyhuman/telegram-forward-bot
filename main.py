from keep_alive import keep_alive
import time
import asyncio
import logging
import sys
import os
import urllib.request
from telethon import TelegramClient, events

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Start keep alive server
keep_alive()
time.sleep(3)  # Give server more time to start

# Telegram bot code starts from here
api_id = 28224513
api_hash = "0a0349ff911e6a1adf144c00d99f668"
session_name = "bot"
from_chat = -1001563681038  # Replace with source chat ID
to_chat = "https://t.me/Human_toss_line"  # Replace with destination channel

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=from_chat))
async def handler(event):
    await client.send_message(to_chat, event.message)

async def main():
    await client.start()
    logger.info("Bot is running...")
    await client.run_until_disconnected()

while True:
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        time.sleep(5)
￼Enter
