import asyncio
import json

from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup
import requests
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import token, egor_id,anna_id

from main import get_data



bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


class UserFunctions(StatesGroup):
    name_state = State()
@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Расписание", "Введите дату"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Расписание", reply_markup=keyboard)

@dp.message_handler(Text(equals="Расписание"))
async def timetable(message: types.Message):
    with open("timetable_dict.json", "r") as file:
        timetable_dict = json.load(file)

    for k, v in (timetable_dict.items()):
        timetable_message = f"{hcode(v['timetable_title'])}"

        await message.answer(timetable_message)

@dp.message_handler(Text(equals="Введите дату"))
async def data_time(message: types.Message):
    await UserFunctions.name_state.set()
# k = input()
    # if message.text == 'Введите дату':
    #     k = message.text
    #     await bot.send_message(user_id, text=f"name")
    # else:
    #     await message.answer("dont")

async def date_update():
    while True:
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        }

        url = "https://sb.bsu.by/raspisanie/map-902_sa.xml"
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")

        timetable = soup.find('div', class_="sw-result")

        r = "Дата обновления 16.11.2022 16:28"
        text_find = timetable.find(text=r)
        if text_find == r:
            await bot.send_message(egor_id, r, disable_notification=True, disable_web_page_preview=True)
            await bot.send_message(anna_id, r, disable_notification=True, disable_web_page_preview=True)

        else:
            await bot.send_message(egor_id, "Please, update timetable!!!")
            await bot.send_message(anna_id, "Please, update timetable!!!")
        await asyncio.sleep(86400)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(date_update())
    executor.start_polling(dp)