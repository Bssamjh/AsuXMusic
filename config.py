from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "13600724")) 
API_HASH = getenv("API_HASH", "ee59fd28d0d065c6b7d105082c6a0ba0")
ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN", "5917639432:AAHy9PssF3SvmkYeSQYg1yszMsLWkBt6qwA")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
LOGGER_ID = int(getenv("LOGGER_ID"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://BS:<password>@cluster0.hjawjqk.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5610994282").split()))
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c5952790fa8235f499749.jpg")
START_IMG = getenv("START_IMG","https://telegra.ph/file/238d26f5188c9056b307b.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AbishnoiMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Abishnoi_bots")
STRING_SESSION = getenv("STRING_SESSION", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1452219013").split()))
