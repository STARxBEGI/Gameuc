
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os

API_TOKEN = os.getenv("BOT_TOKEN")  # Railway environmentdan oladi

# Logging
logging.basicConfig(level=logging.INFO)

# Bot va dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Start komandasi
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f"Salom {name}, anime kodini yuboring.")

# Main
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
