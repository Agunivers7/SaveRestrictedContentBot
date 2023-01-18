#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 10651048
API_HASH = "37775aca7d11f450ecde375baac17fe7"
BOT_TOKEN = "5743646572:AAEn0QWcJtEMN3EbRRj_rNoshdhRZfqrKb8"
SESSION = "1BVtsOJgBuzs0kfiQiv90P_ylBYh7gH9Oi7WHg-raxSDjbEhr-3634DGjfIgbCjrg87LSbly8UjkrrTuFUg303qfCzGoVXi5dMFf3ysUEiQEu3KSAWPO595iBjdurpulECDHLakYzpT1Ooms7RNr-apCZtZA77s0lJt0SfOb6Fjpq3XEuknL5NLA8YA_f9oaIbKeM9DpLXkVmlFejTQizB6wBNLIrPclwStYwe06LIqAPOpke9RF5RWrDsbH15OuP_RvLEb231PcchvYmqSuuVGLOAhOjGnLhnmxVtZFFbRKVna7RgbKYy1PTxsvU8n3IH3BNKGY6_Lv58t0oI0a8JAVzAzJoVjE="
FORCESUB = "Agunivers_fransis"
AUTH = 1323557247

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
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
    print(e)
    sys.exit(1)
