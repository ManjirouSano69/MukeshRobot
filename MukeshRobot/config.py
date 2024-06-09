
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "22867431" # integer value, dont use ""
    API_HASH = "24ef0e76ceb137563dc33722e4cd79bd"
    TOKEN = "7483130894:AAH9VSFstcInQmPS2NGEKv5ivcq_XtAfkx8"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5743248220 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "ichigo_Support_Group"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph/file/22bb1d13284399ee80740.jpg"
    EVENT_LOGS = (-1002197525160)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://itsintrovert07:ichigo@cluster0.psjfsgj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # RECOMMENDED
    DATABASE_URL = "postgres://dulfvtph:lyqfQJQwBjpPnYKhfmDTn7bJg37_vF_c@kesavan.db.elephantsql.com/dulfvtph"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "Q6MOGXAIEARCE2YB"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "OV99NVF77YZK"
    
    # Get your API key from https://timezonedb.com/api


    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = ["7429244757"]  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
