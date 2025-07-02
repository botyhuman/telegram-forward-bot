from keep_alive import keep_alive
import asyncio
import logging
import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Start keep_alive HTTP server
keep_alive()

# Env vars from Render
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
session_string = os.environ.get("SESSION_STRING")

# Chat IDs
from_chat = -1001563681038
to_chat = "https://t.me/Human_toss_line"

# Create client using StringSession
client = TelegramClient(StringSession(session_string), api_id, api_hash)

@client.on(events.NewMessage(chats=from_chat))
async def handler(event):
    await client.send_message(to_chat, event.message)

async def main():
    await client.start()
    logger.info("Bot is running...")
    await client.run_until_disconnected()

# Run bot
asyncio.get_event_loop().run_until_complete(main())
