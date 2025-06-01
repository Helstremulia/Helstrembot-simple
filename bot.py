import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

user_data = {}

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_data[message.chat.id] = {}
    await message.answer("Привет! Введи дату рождения (ГГГГ-ММ-ДД):")

@dp.message_handler(lambda message: message.chat.id in user_data and "date" not in user_data[message.chat.id])
async def handle_date(message: types.Message):
    user_data[message.chat.id]["date"] = message.text
    await message.answer("Теперь введи время рождения (например, 14:30):")

@dp.message_handler(lambda message: message.chat.id in user_data and "time" not in user_data[message.chat.id])
async def handle_time(message: types.Message):
    user_data[message.chat.id]["time"] = message.text
    await message.answer("И наконец, город рождения:")

@dp.message_handler(lambda message: message.chat.id in user_data and "place" not in user_data[message.chat.id])
async def handle_place(message: types.Message):
    user_data[message.chat.id]["place"] = message.text
    await message.answer("Спасибо! Данные получены ✅")

    # Выводим в консоль
    print(f"Пользователь {message.chat.id}: {user_data[message.chat.id]}")
    user_data.pop(message.chat.id)

if name == "__main__":
    executor.start_polling(dp, skip_updates=True)
