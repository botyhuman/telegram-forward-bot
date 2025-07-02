from keep_alive import keep_alive
import asyncio
import logging
import os
from telethon import TelegramClient, events

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Start keep_alive server
keep_alive()

# Telegram credentials
api_id = 28224513
api_hash = "0a0349ff911e6a1adf144c00d99f668"
session_string = "1BVts0GQBU0Hnm1HAwEuM5EJK2pI6VvVCFvWTck6H6W0vr5xparz3M2LzwWBK1SeniUN-Ruj8rDmy5140j-wAwQ4pjyYg1bTqRigufQKhxKEQ6b90091DJ4TURlewnAPjtDBE4m0x0nd-nN0wdIx6003xtR60dwt7ud0nThe4GeAr0dkc677CmfgzgAfGA51KmXKeuu6cgKKjT0jzZVeer0tRa03005hLP-y3z39sCz7sPS16JRMOCYxcR_HfXq6jQt-q2LQ8ziCVjngqwYPZ6yTwCk2s-yTTFHc1f6zIA-cxDFSt9HJbe4AEgWZ7PHW_7b3KgNX8QD1x1sZCnIk7UswBpIB1BVU="

# Source and destination
from_chat = -1001563681038
to_chat = "https://t.me/Human_toss_line"

# Create client with string session
client = TelegramClient(session_string, api_id, api_hash)

@client.on(events.NewMessage(chats=from_chat))
async def handler(event):
    await client.send_message(to_chat, event.message)

async def main():
    await client.start()
    logger.info("Bot is running...")
    await client.run_until_disconnected()

# Start loop
asyncio.get_event_loop().run_until_complete(main()) 
