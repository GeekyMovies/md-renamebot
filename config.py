import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", "23311160"))
    API_HASH = os.environ.get("API_HASH" "2a1366013eca4256bce853346dbcda49")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5914875548:AAF9MzN2Mk8QQhkalABpz_45MjQjBnQUOqg")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5691018873"))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", None)
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Geekymovies:Geekymovies@cluster0.7llffit.mongodb.net/?retryWrites=true&w=majority")
    
