import os
import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("NO TOKEN")
    exit()

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def handler(message: types.Message):
    await message.answer("😈 KROKHINA bot v2 работает")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
