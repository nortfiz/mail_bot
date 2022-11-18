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
        rasp = f"\n{hbold(v['timetable_title0'])}" \
               f"\n{hcode(v['timetable_title1'])}"\
               f"\n{hcode(v['timetable_title2'])}"\
               f"\n{hbold(v['timetable_title3'])}"\
               f"\n{hcode(v['timetable_title4'])}"\
               f"\n{hcode(v['timetable_title5'])}"\
               f"\n{hcode(v['timetable_title6'])}"\
               f"\n{hbold(v['timetable_title7'])}"\
               f"\n{hcode(v['timetable_title8'])}"\
               f"\n{hcode(v['timetable_title9'])}"\
               f"\n{hcode(v['timetable_title10'])}"\
               f"\n{hcode(v['timetable_title11'])}"\
               f"\n{hbold(v['timetable_title12'])}"\
               f"\n{hcode(v['timetable_title13'])}"\
               f"\n{hcode(v['timetable_title14'])}"\
               f"\n{hcode(v['timetable_title15'])}"\
               f"\n{hcode(v['timetable_title16'])}"\
               f"\n{hbold(v['timetable_title17'])}"\
               f"\n{hcode(v['timetable_title18'])}"\
               f"\n{hcode(v['timetable_title19'])}"\
               f"\n{hbold(v['timetable_title20'])}"\
               # f"\n{hcode(v['timetable_title21'])}"\
               # f"\n{hcode(v['timetable_title22'])}"\
               # f"\n{hcode(v['timetable_title23'])}"

    await message.answer(rasp)


if __name__ == '__main__':
    executor.start_polling(dp)