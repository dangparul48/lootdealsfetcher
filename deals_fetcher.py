'''
This script will keep fetching new messages from top
telegram channels like FRCP etc. and if there are any LOOT deals,
will forward them to a separate channel
'''
from telethon import TelegramClient
import time
import re


api_id = 1111111  # needs to be replaced
api_hash = "this#is#my#api#hash"  # needs to be replaced
client = TelegramClient("hitele", api_id, api_hash)
client.start()


async def main():
    '''
    client.iter_dialogs() return the list of all the chats you've opened in your telegram
    or channels that you've subscribed to
    '''
    while True:
        async for dialog in client.iter_dialogs():
            if dialog.title == "FRCP":
                unread_count = dialog.unread_count
                print(f"{unread_count} new messages(s) found")
                if unread_count > 0:
                    async for message in client.iter_messages(dialog.title, limit=unread_count):
                        if message.text is not None:
                            if re.search("LO+T", message.text.upper()):
                                await message.forward_to("@topamazdeals")
                        await message.mark_read()
                else:
                    time.sleep(2)


# Main program trigger
with client:
    client.loop.run_until_complete(main())
