import asyncio
from scheduler import SchedulerWrapper
from datetime import datetime, timedelta

from aiogram import Dispatcher, Bot
from aiogram.filters import Command

bot = Bot(token="telegram_bot_token")

dp = Dispatcher()

print("started")

async def my_function(message) -> None:
    print("Scheduled task is being executed!")
    await message.answer("Scheduled task is being executed!")

@dp.message(Command("schedule"))
async def handler(message):
    job = SchedulerWrapper().add_job(
        my_function,
        "date",
        run_date=datetime.now() + timedelta(seconds=3),
        args=[message]
    )
    print(job)
    await message.answer("Job scheduled!")

async def main():
    await dp.start_polling(bot)


asyncio.run(main())