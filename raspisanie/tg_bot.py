import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from config import token, user_id



bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Расписание", "Введите дату"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Расписание", reply_markup=keyboard)

@dp.message_handler(Text(equals="Расписание"))
async def timetable(message: types.Message):
    with open("timetable_dict.json") as file:
        timetable_dict = json.load(file)

    for k, v in (timetable_dict.items()):
        rasp = f"\n{hunderline(v['timetable_date'])}" \
               f"\n{hcode(v['timetable_title'])}"

    await message.answer(rasp)


if __name__ == '__main__':
    executor.start_polling(dp)