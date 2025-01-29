from aiogram import Bot, Dispatcher, types
from aiogram import executor
from config import TOKEN
from db_sqlite3 import insert_into_table_user
from db_sqlite3 import insert_into_table_city
from requests_weather import get_weather
import asyncio
import datetime


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды")

    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_surname = message.from_user.last_name
    username = message.from_user.username
    date_time = datetime.datetime.today()

    insert_into_table_user(user_id, user_name, user_surname, username, date_time)


@dp.message_handler()
async def weather_handler(message: types.Message):
    try:
        city = message.text.strip()
        weather = get_weather(city)

        await message.reply(f"Погода в {city}:\n{weather}")

        user_id = message.from_user.id
        insert_into_table_city(user_id, city)

    except IndexError:
        await message.reply("Используй формат: /weather [город]")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)