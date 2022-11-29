import asyncio
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData
from bs4 import BeautifulSoup
import requests
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import token, egor_id
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from main import update_date, get_data


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
cb = CallbackData('kb_data', 'action')
@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Расписание", "Выберите начало недели", "Дата обновления"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Расписание", reply_markup=keyboard)
    # test

@dp.message_handler(Text(equals="Расписание"))
async def timetable(message: types.Message):
    with open("timetable_dict.json", "r") as file:
        timetable_dict = json.load(file)

    for k, v in (timetable_dict.items()):
        timetable_message = f"{hcode(v['timetable_title'])}"

        await message.answer(timetable_message)

@dp.message_handler(Text(equals="Дата обновления"))
async def data_time(message: types.Message):
    get_data()
    while True:
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        }

        url = "https://sb.bsu.by/raspisanie/map-902_sa.xml"
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")

        r = "Дата обновления 29.11.2022 11:08"
        text_find = timetable.find(text=r)
        if text_find == r:
            await message.answer(r, disable_notification=True, disable_web_page_preview=True)
            # await bot.send_message(anna_id, r, disable_notification=True, disable_web_page_preview=True)
            break
        else:
            await bot.send_message(egor_id, "Please, update timetable!!!")
            # await bot.send_message(anna_id, "Please, update timetable!!!")
            break

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

        r = "Дата обновления 29.11.2022 11:08"
        text_find = timetable.find(text=r)
        if text_find == r:
            await bot.send_message(egor_id, r, disable_notification=True, disable_web_page_preview=True)
            # await bot.send_message(anna_id, r, disable_notification=True, disable_web_page_preview=True)

        else:
            await bot.send_message(egor_id, "Please, update timetable!!!")
            # await bot.send_message(anna_id, "Please, update timetable!!!")
        await asyncio.sleep(86400)

@dp.message_handler(Text(equals="Выберите начало недели"))
async def data_time(message: types.Message):
    with open("timetable_date.json", "r") as file:
        timetable_date = json.load(file)
        kb_data = InlineKeyboardMarkup()
        for k, v in (timetable_date.items()):
            q = f"{v['date_now']}"
            kb_data.add(InlineKeyboardButton(f'{q}', callback_data=f'{q}'))
        await message.answer("Выберите дату:", reply_markup=kb_data)

@dp.callback_query_handler(lambda callback_query: callback_query.data == '21.11.2022')
async def callback_kb_data(callback: types.CallbackQuery) -> None:
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }

    url = "https://sb.bsu.by/raspisanie/map-902_sa.xml"
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    timetable_dict = {}

    timetable = soup.find("tbody").find_all("tr", vl="21.11.2022")
    k = 1
    for i in range(21):
        id = timetable[i].text

        timetable_dict[k] = {
            "timetable_title": id
        }
        k += 1

    with open("timetable_dict_date.json", "w") as file:
        json.dump(timetable_dict, file, indent=1, sort_keys=True, ensure_ascii=False)
    with open("timetable_dict_date.json", "r") as file:
        timetable_dict = json.load(file)

    for k, v in (timetable_dict.items()):
        timetable_message = f"{hcode(v['timetable_title'])}"
        await callback.message.answer(timetable_message)

@dp.callback_query_handler(lambda callback_query: callback_query.data == '28.11.2022')
async def callback_kb_data(callback: types.CallbackQuery) -> None:
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }

    url = "https://sb.bsu.by/raspisanie/map-902_sa.xml"
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    timetable_dict = {}

    timetable = soup.find("tbody").find_all("tr", vl="28.11.2022")
    k = 1
    for i in range(19):
        id = timetable[i].text

        timetable_dict[k] = {
            "timetable_title": id
        }
        k += 1

    with open("timetable_dict_date.json", "w") as file:
        json.dump(timetable_dict, file, indent=1, sort_keys=True, ensure_ascii=False)
    with open("timetable_dict_date.json", "r") as file:
        timetable_dict = json.load(file)

    for k, v in (timetable_dict.items()):
        timetable_message = f"{hcode(v['timetable_title'])}"
        await callback.message.answer(timetable_message)

@dp.callback_query_handler(lambda callback_query: callback_query.data == '05.12.2022')
async def callback_kb_data(callback: types.CallbackQuery) -> None:
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }

    url = "https://sb.bsu.by/raspisanie/map-902_sa.xml"
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    timetable_dict = {}

    timetable = soup.find("tbody").find_all("tr", vl="05.12.2022")
    k = 1
    for i in range(18):
        id = timetable[i].text

        timetable_dict[k] = {
            "timetable_title": id
        }
        k += 1

    with open("timetable_dict_date.json", "w") as file:
        json.dump(timetable_dict, file, indent=1, sort_keys=True, ensure_ascii=False)
    with open("timetable_dict_date.json", "r") as file:
        timetable_dict = json.load(file)

    for k, v in (timetable_dict.items()):
        timetable_message = f"{hcode(v['timetable_title'])}"
        await callback.message.answer(timetable_message)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.create_task(date_update())
    update_date()
    get_data()
    executor.start_polling(dp)
