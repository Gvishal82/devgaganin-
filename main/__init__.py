#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

# variables
API_ID = "10000844" #config("API_ID", default=None, cast=int)
API_HASH = "776f257fc1d1f8aa4aea9dd35d10a45b" #config("API_HASH", default=None)
BOT_TOKEN = "7311703567:AAHhEoFLB1k84UQxXib1HLnWa0IIHbFfmXA" #config("BOT_TOKEN", default=None)
SESSION = "BQF2s3oAKwMrDulQAieZ0_lxoaCiH2fepp95u_lwzQVAz9hrmnWmULIrG4QAbzo2CCfmPsuB49gF_c8epQryM_oSzaHVPn_HXQFPHsCwCOqhU4ZZjZm5uOaXwKarzqNmly3wQUav1BPg0GidvJN1ztrmh1XMGSbNb8StG_v2DF49zjdibeOg2LCoU0ckjwEYpqdjxhlTPedOkCflCssMDJZBdoMXT9cFiiOYwGOSwXAsSu_QQQG8N05NIA153qwePXeTHYRyC6ac5N9f0LPNSYwgeaB6aKV5EgcmIyLj7a0hhDn4YBwxZp1XhhI1-XxY0Ex37eBnctI-rCQ_9ufiDdxQCmKwEAAAAAFsWSMcAA" #config("SESSION", default=None)
FORCESUB = "Restricted_content_bot1" #config("FORCESUB", default=None)
AUTH = "7141612609" #config("AUTH", default=None)

SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    # print(e)
    # logger.info(e)
    sys.exit(1)
