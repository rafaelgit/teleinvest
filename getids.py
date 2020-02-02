#!/usr/local/bin/python3
from telethon import TelegramClient
import os

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')

client = TelegramClient('anon', api_id, api_hash)

async def main():
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

with client:
    client.loop.run_until_complete(main())