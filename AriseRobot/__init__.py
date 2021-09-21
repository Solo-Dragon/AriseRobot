import os
from pyrogram import Client

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
TOKEN = os.environ.get("TOKEN", None)
ME_ID = int(os.environ.get('ME_ID', 1775659407))
#dude i aint a racist just for fun
NIGGERS = {int(x) for x in os.environ.get("NIGGERS", "").split()}
NIGGERS.add(ME_ID)

ARISE = Client(':memory:', api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
