import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("SECRET_KEY")
# Экземпляр == Объект
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Асинхронное программирование
@dp.message(Command("start"))
async def cmd_start(msg: Message):
    await msg.answer("Привет!")


@dp.message(Command("info"))
async def author(msg: Message):
    await msg.reply("Автор: Шох")


@dp.message(Command("dice"))
async def cmd_dice(message: Message):
    await message.answer_dice(emoji="🎲")


# Процедурное программирование

# def cmd_start(message: Message):
#     return message.answer("Hello!")
#
#
# cmd_start()


async def bot_run():
    await dp.start_polling(bot)


if __name__ == "__main__":
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)
    asyncio.run(bot_run())
