#!/usr/local/bin/python3
from telethon import TelegramClient, events
import os

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')

client = TelegramClient('session_name', api_id, api_hash)
client.start()

@client.on(events.NewMessage)
async def main(event):
    if (event.chat_id == 1):
        await event.forward_to(2)

with client:
    client.run_until_disconnected()