import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('SECRET_KEY')

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
