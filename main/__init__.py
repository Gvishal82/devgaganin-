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
API_ID = 10000844 #config("API_ID", default=None, cast=int)
API_HASH = "776f257fc1d1f8aa4aea9dd35d10a45b" #config("API_HASH", default=None)
BOT_TOKEN = "7311703567:AAHhEoFLB1k84UQxXib1HLnWa0IIHbFfmXA" #config("BOT_TOKEN", default=None)
SESSION = "BQF2s3oArWcMuycFC_bQoqKv0Brhd4f4CkaQlOqrOGoTIdmtxrNShiTIGJTEm8p6tiNTHF1A6fBvho8B8vH1utig2JIZMlHOsaG_Ro-VL7lfEkCIsGpK-kxNah3e7KZ_PMHGit16j3irdZGvN6lFfpA-Y_AmXKCWEC6BdwjilaKOVNsPi5iJ4Y0DvChgtfYDcISx5dk-t0_BtWfs2h0Fh5ike8-b-4s-UxdvZ_39yeFyAG_rFcB12w9K88YXj3hMwOT30spC2Gc7mzZPGjSGCEkvi8F3yGNs5m9jpGyYH5LaCgkl-SjGVqA-1T7LyhfVg9RNjOqQHA0-pL_ZwZh01aZ7ATXjaQAAAAFsWSMcAA" #config("SESSION", default=None)
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
