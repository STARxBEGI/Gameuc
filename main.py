
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3

API_TOKEN = "8168132813:AAFy0RwWSc6m4_ddP28Lpwi9JSJLIWu62U4"
ADMIN_IDS = [7809052580, 7516122894]
CHANNEL_LINK = "https://t.me/ANIMUZ_ANIMELAR"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

conn = sqlite3.connect("anime.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS anime (code TEXT, name TEXT, total_eps INTEGER, lang TEXT, image TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS episodes (code TEXT, video TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS shorts (video TEXT)''')
conn.commit()

def get_keyboard(user_id):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("Anime izlash"), KeyboardButton("Kod yuborish"), KeyboardButton("Shorts"))
    if user_id in ADMIN_IDS:
        kb.add(KeyboardButton("Anime yasash"), KeyboardButton("Qism qo‘shish"))
        kb.add(KeyboardButton("Post tayyorlash"), KeyboardButton("Shorts qo‘shish"))
    return kb

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    kb = get_keyboard(message.from_user.id)
    await message.answer(f"Salom {message.from_user.first_name}, anime kodini yuboring", reply_markup=kb)

@dp.message_handler(lambda message: message.text == "Anime izlash")
async def search_anime(message: types.Message):
    await message.answer("Kanalga o‘tayapsiz...", reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f"<a href='{CHANNEL_LINK}'>Anime Kanal</a>", parse_mode='HTML')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
