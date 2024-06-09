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
BOT_TOKEN = "7341520063:AAGMUQBtz8z5pIqDMs7p5kIOHxHKu5ECh6U" #config("BOT_TOKEN", default=None)
SESSION = "BQGtpF0Atbhw6pSY_cWvDLYDiuR5jLAcpLmp4eb7xOsGtc0c3-mVWMF__QxUwYWlskZMWRajuWAb_Sg1NHm00a3ajDMX3GsSwn-0ZzvLeWQ7x76LDqDbRFH8VyB5bPvFT9zGOzAn5JvPzsnrWE_iOZNqyCZC0fKErOmSgEPCfoDXr12OGoCZm_a-exKRuEizr9KuaOOtYw8jfhnZT3mFT4LhIPrZ8pbXgJDNGU1xBzjCRmEcfs-DWat_86JqQw5_3ovWIGXvpgRrVKMxjtlB05pA9RHHQFTTLoNXh5CXOPymZ-XmaAxBQIsu_C2YggzsN-zW6ytMLLBVSoklp-_TWpVbYxgAEwAAAAG1IkhdAA" #config("SESSION", default=None)
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
