import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import (Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,
                           InlineKeyboardButton)
from aiogram.filters import Command, CommandStart

import os
from dotenv import load_dotenv
load_dotenv()

Token = os.getenv("Token")
menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='salem'), KeyboardButton(text="alem")],
        [KeyboardButton(text="jardem")],
    ],
    resize_keyboard=True
)

nline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='👋 Salomlashish', callback_data='say_hi')],
        [InlineKeyboardButton(text='📢 Kanalimiz', url='https://t.me/BotFather')]
    ]
)

# 'alem' uchun menyu
line_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🌍 Dunyo yangiliklari', url='https://t.me/BotFather')],
        [InlineKeyboardButton(text='📊 Statistika', callback_data='stats')]
    ]
)

# 'jardem' uchun menyu
jardem_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='👤 Admin bilan bog‘lanish', url='https://t.me/dilnoza_kulbaeva')],
        [InlineKeyboardButton(text='❓ Ko‘p beriladigan savollar', callback_data='faq')]
    ]
)

bot = Bot(token=Token)
dp = Dispatcher()
@dp.message(CommandStart())
async def start(messege:Message):
    await messege.answer(f"hello {messege.from_user.username}", reply_markup=menu)
@dp.message(Command("help"))
async def help(messege:Message):
    await messege.answer("qanday jardem kerek? ")

@dp.message()
async def menyular(message: Message):
    t = message.text

    if t == "salem":
        await message.answer("✨ **Salem** bo'limiga xush kelibsiz!", reply_markup=nline_menu)

    elif t == "alem":
        await message.answer("🌐 **Alem** bo'limi ma'lumotlari:", reply_markup=line_menu)

    elif t == "jardem":
        await message.answer("🆘 **Jardem** (Yordam) kerakmi?", reply_markup=jardem_inline)



async def main():
    print("...")
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
