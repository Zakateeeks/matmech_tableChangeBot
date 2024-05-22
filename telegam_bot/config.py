from aiogram import Bot, Dispatcher
import configparser

config = configparser.ConfigParser()
config.read('../data.ini')

API_TOKEN = config["BOT"]["BOT_API"]
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
