import os

from dotenv import load_dotenv

load_dotenv("../../")

# Path
SRC_PTH = os.path.abspath("src")

# Discord Bot
BOT = {
    "token": os.getenv("BOT_TOKEN"),
    "prefix": "!",
}

# Stock Market API
SM_API = {
    "token": os.getenv("SM_API_TOKEN"),
    "url": "https://api.tiingo.com",
}

# Database
DB = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "name": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}
