import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7707602224:AAFNdClhpd0wGJXEmDFwPFKok2bdbdvxpiI")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20071888"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1c4cb9d94b23282abd9ae2a87a521b53")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002335544406"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7040944963"))

#Port
PORT = os.environ.get("PORT", "3010")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://5foot:5foot80@5foot.q69w2.mongodb.net/?retryWrites=true&w=majority")
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", "mongodb+srv://5foot:5foot80@5foot.q69w2.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "5foot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002467223104"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002947747406"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>hey {first}\n\nI am a file storing Bot</b>.")
try:
    ADMINS=[1439206175]
    for x in (os.environ.get("ADMINS", "7040944963").split()):
        ADMINS.append(int(7040944963))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>you need to send join request to these channels</b>\n\n<b>please send join request to these channels</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ please don't text I am a file storing bot"

ADMINS.append(OWNER_ID)
ADMINS.append(1439206175)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


