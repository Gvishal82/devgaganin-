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
BOT_TOKEN = "7456514220:AAGg5MHY8x-ull2pm9RZjGMwB0rN9t976DE" #config("BOT_TOKEN", default=None)
SESSION = "AQCYmcwAdKJQ7HjB1Eq431Eq1zQGpVpEnNIR6cspElo6ozxpRUA6K156UWAGmKFmWWDwbehI02zfEBNBIoxNX_zUbWCicQt9ZIHT1tXqqQKKVitPjqp0GuJ8wVtCkYIQaoJjLd8xySSAS9_gZo1tV4BRn6lpeHvh0BokxM-_l2RnUvueiLea5rdEiOXfh2xcbd27TphAUcJOa7sr77xbnDlklreHtjbBn9OaVHu1BdoatRBuMjLqUB2a-_V0NSQZ6H1LwUrjfnPQiQe76N36HPSkq91bdKYuVX2VYEryZX7XzL_MHxi2MftCt8eTftTwYT7YiueJ3Jw0FMuYOKdvszo8rqRRQgAAAAGprFxBAA" #config("SESSION", default=None)
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
