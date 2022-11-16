import asyncio
import json

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from config import token, user_id
import datetime
from main import chek_new_update


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Все новости", "Последние 5 новостей", "Свежие новости"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Лента новостей", reply_markup=keyboard)

@dp.message_handler(Text(equals="Все новости"))
async def get_all_news(message: types.Message):
    with open("news_dict.json") as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items()):
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}" \
               f"\n{hunderline(v['article_title'])}" \
               f"\n{hcode(v['article_desc'])}" \
               f"\n{hlink(v['article_title'], v['article_url'])}"

        await message.answer(news, disable_web_page_preview=True)


@dp.message_handler(Text(equals="Последние 5 новостей"))
async def get_last_five_news(message: types.Message):
    with open("news_dict.json") as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[-5:]:
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}" \
               f"\n{hunderline(v['article_title'])}" \
               f"\n{hcode(v['article_desc'])}" \
               f"\n{hlink(v['article_title'], v['article_url'])}"

        await message.answer(news, disable_web_page_preview=True)

@dp.message_handler(Text(equals="Свежие новости"))
async def get_fresh_news(message: types.Message):
    fresh_news = chek_new_update()
    if len(fresh_news) >= 1:
        for k, v in sorted(fresh_news.items()):
            news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}" \
                   f"\n{hunderline(v['article_title'])}" \
                   f"\n{hcode(v['article_desc'])}" \
                   f"\n{hlink(v['article_title'], v['article_url'])}"

            await message.answer(news, disable_web_page_preview=True)
    else:
        await message.answer("Новых новостей нет")

async def news_every_hour():
    while True:
        fresh_news = chek_new_update()

        if len(fresh_news) >= 1:
            for k, v in sorted(fresh_news.items()):
                news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}" \
                   f"\n{hunderline(v['article_title'])}" \
                   f"\n{hcode(v['article_desc'])}" \
                   f"\n{hlink(v['article_title'], v['article_url'])}"

                # get @userinfobot
                await bot.send_message(user_id, news, disable_notification=True, disable_web_page_preview=True)
        else:
            await bot.send_message(user_id, "Пока нет свежих новостей", disable_notification=True)

        await asyncio.sleep(1800)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_hour())
    executor.start_polling(dp)
