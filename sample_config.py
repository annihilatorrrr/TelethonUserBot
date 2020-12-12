# PLEASE STOP!
# DO NOT EDIT THIS FILE
# Create a new config.py file in same dir and import, then extend this class.
import os
from distutils.util import strtobool as sb


class Config:
    LOGGER = True
    # Get this value from my.telegram.org! Please do not steal
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    # string session for running on Heroku
    # some people upload their session files on GitHub or other third party hosting
    # websites, this might prevent the un-authorized use of the
    # confidential session files
    HU_STRING_SESSION = os.environ.get("HU_STRING_SESSION", None)
    # Get your own APPID from https://api.openweathermap.org/data/2.5/weather
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    # Send .get_id in any group to fill this value.
    PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID", None)
    if PRIVATE_GROUP_BOT_API_ID:
        PRIVATE_GROUP_BOT_API_ID = int(PRIVATE_GROUP_BOT_API_ID)
    # tag channel
    TAG_CHANNEL = os.environ.get("TAG_CHANNEL", None)
    if TAG_CHANNEL:
        TAG_CHANNEL = int(TAG_CHANNEL)
    # Send .get_id in any channel to fill this value. ReQuired for @Manuel15 inspiration to work!
    PRIVATE_CHANNEL_BOT_API_ID = os.environ.get(
        "PRIVATE_CHANNEL_BOT_API_ID", None)
    if PRIVATE_CHANNEL_BOT_API_ID:
        PRIVATE_CHANNEL_BOT_API_ID = int(PRIVATE_CHANNEL_BOT_API_ID)
    # This is required for the plugins involving the file system.
    TMP_DOWNLOAD_DIRECTORY = os.environ.get(
        "TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
    # This is required for the speech to text module. Get your USERNAME from https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    IBM_WATSON_CRED_USERNAME = os.environ.get("IBM_WATSON_CRED_USERNAME", None)
    # This is required for the hash to torrent file functionality to work.
    HASH_TO_TORRENT_API = os.environ.get(
        "HASH_TO_TORRENT_API", "https://example.com/torrent/{}")
    # This is required for the @telegraph functionality.
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "UniBorg")
    # Get a Free API Key from OCR.Space
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    # Send .get_id in any group with all your administration bots (added)
    G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", None)
    if G_BAN_LOGGER_GROUP:
        G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)
    # TG API limit. An album can have atmost 10 media!
    TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
    # Telegram BOT Token from @BotFather
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    #
    NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
    #
    # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
    # TG API limit. A message can have maximum 4096 characters!
    MAX_MESSAGE_SIZE_LIMIT = 4095
    # set blacklist_chats where you do not want userbot's features
    UB_BLACK_LIST_CHAT = {int(x) for x in os.environ.get(
        "UB_BLACK_LIST_CHAT", "").split()}
    # specify LOAD and NO_LOAD
    LOAD = []
    # folowing plugins won't work on Heroku,
    # because of their ephemeral file system
    NO_LOAD = [
        "antispam"
    ]
    # Get your own API key from https://www.remove.bg/ or
    # feel free to use http://telegram.dog/Remove_BGBot
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    # For Databases
    # can be None in which case plugins requiring
    # DataBase would not work
    DB_URI = os.environ.get("DATABASE_URL", None)
    # number of rows of buttons to be displayed in .helpme command
    NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(
        os.environ.get("NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD", 5))
    # specify command handler that should be used for the plugins
    # this should be a valid "regex" pattern
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "\.")
    # specify list of users allowed to use bot
    # WARNING: be careful who you grant access to your bot.
    # malicious users could do ".exec rm -rf /*"
    SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
    # VeryStream only supports video formats
    VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
    VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)
    # Google Drive ()
    IS_TEAM_DRIVE = os.environ.get("IS_TEAM_DRIVE", False)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    #
    TELE_GRAM_2FA_CODE = os.environ.get("TELE_GRAM_2FA_CODE", None)
    #
    GROUP_REG_SED_EX_BOT_S = os.environ.get(
        "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot")
    # rapidleech plugins
    OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", "0")
    OPEN_LOAD_KEY = os.environ.get("OPEN_LOAD_KEY", "0")
    # Google Chrome Selenium Stuff
    # taken from https://github.com/jaskaranSM/UniBorg/blob/9072e3580cc6c98d46f30e41edbe73ffc9d850d3/sample_config.py#L104-L106
    GOOGLE_CHROME_DRIVER = os.environ.get("GOOGLE_CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)
    # spotify stuff
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    SPOTIFY_INITIAL_BIO = os.environ.get("SPOTIFY_INITIAL_BIO", None)
    SPOTIFY_BIO_PREFIX = os.environ.get("SPOTIFY_BIO_PREFIX", None)
    SPOTIFY_KEY = os.environ.get("SPOTIFY_KEY", None)
    SPOTIFY_DC = os.environ.get("SPOTIFY_DC", None)

    LYDIA_API = os.environ.get("LYDIA_API", None)
    DEFAULT_NAME = os.environ.get("DEFAULT_NAME", None)
    #
    # define "spam" in PMs
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    # leave this blank, should be automatically filled for Heroku.com users
    PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID", None)
    if PM_LOGGR_BOT_API_ID:
        PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
    # define the "types" that should be uplaoded as streamable
    TL_VID_STREAM_TYPES = ("MKV", "MP4", "WEBM")
    TL_MUS_STREAM_TYPES = ("MP3", "WAV", "FLAC")
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    ANTI_SPAMBOT = os.environ.get("ANTI_SPAMBOT", None)
    ANTI_SPAMBOT_SHOUT = os.environ.get("ANTI_SPAMBOT_SHOUT", None)
    # API_TOKEN for quote plugin
    API_TOKEN = os.environ.get("API_TOKEN", None)
    # MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
    BOTLOG = os.environ.get("BOTLOG", None)
    # MONGOCLIENT = pymongo.MongoClient(MONGO_DB_URI)
    # MONGO = MONGOCLIENT.userbot
    # MIRRORACE KEY
    MIRROR_ACE_API_KEY = os.environ.get("MIRROR_ACE_API_KEY", None)
    MIRROR_ACE_API_TOKEN = os.environ.get("MIRROR_ACE_API_TOKEN", None)
    # RSS_POST_MSG_GROUP_ID = map(int, os.environ.get("RSS_POST_MSG_GROUP_ID", None).split())
    RSS_POST_MSG_GROUP_ID = os.environ.get("RSS_POST_MSG_GROUP_ID", None)
    if RSS_POST_MSG_GROUP_ID:
        RSS_POST_MSG_GROUP_ID = int(RSS_POST_MSG_GROUP_ID)
    SPAM_WATCH_API = os.environ.get("SPAM_WATCH_API", None)
    SPAM_WATCHAPI = os.environ.get("SPAM_WATCHAPI", None)
    SPAM_WATCH_LOG_CHANNEL = os.environ.get("SPAM_WATCH_LOG_CHANNEL", None)
    if SPAM_WATCH_LOG_CHANNEL:
        SPAM_WATCH_LOG_CHANNEL = int(SPAM_WATCH_LOG_CHANNEL)
    # Userbot logging feature switch.
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", None))
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)

    # Google Photos ()
    G_PHOTOS_CLIENT_ID = os.environ.get("G_PHOTOS_CLIENT_ID", None)
    G_PHOTOS_CLIENT_SECRET = os.environ.get("G_PHOTOS_CLIENT_SECRET", None)
    G_PHOTOS_AUTH_TOKEN_ID = int(
        os.environ.get("G_PHOTOS_AUTH_TOKEN_ID", "-100"))
    # Heroku stuff
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    # for video trimming and screenshot plugins
    FF_MPEG_DOWN_LOAD_MEDIA_PATH = os.environ.get(
        "FF_MPEG_DOWN_LOAD_MEDIA_PATH", None)
    INSTA_ID = os.environ.get("INSTA_ID", None)
    INSTA_PASS = os.environ.get("INSTA_PASS", None)


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
