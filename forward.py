#!/usr/local/bin/python3
from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
received_ids = os.getenv('RECEIVED_IDS')
forward_id = os.getenv('FORWARD_ID')

client = TelegramClient('session_name', api_id, api_hash)
client.start()

@client.on(events.NewMessage)
async def main(event):
    print(event.chat_id)
    if (received_ids.find(str(event.chat_id)) >= 0):
        await event.forward_to(int(forward_id))

with client:
    client.run_until_disconnected()