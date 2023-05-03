from aiogram import types
from aiogram.dispatcher.filters import Text
import requests
from datetime import datetime
from main import bot, dp


@dp.message_handler(commands=['start'])
async def start_msg(message: types.Message):
    await bot.send_message(message.chat.id, 'Привет! Напиши /help, чтобы узнать функции бота!')


@dp.message_handler(commands=['help'])
async def help_msg(message: types.Message):
    await bot.send_message(message.chat.id, "Функции бота:\n"
                "/price - цена покупки и продажи BTC\n"
                "/statistics - статистика за последние 24 часа")


@dp.message_handler(commands=['price'])
async def price_msg(message: types.Message):
    try:
        req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
        response = req.json()
        print(response)
        sell_price = response['btc_usd']['sell']
        buy_price = response['btc_usd']['buy']
        await bot.send_message(message.chat.id,
            "Дата: "
            f"{datetime.now().strftime('%d.%m.%Y %H:%M')}\nЦена продажи 1 BTC: {'%.2f' % sell_price} USD\n"
            f"Цена покупки 1 BTC: {'%.2f' % buy_price} USD")
    except Exception as ex:
        print(ex)
        await bot.send_message(message.chat.id,
            'Что-то пошло не так, попробуйте позже...')


@dp.message_handler(commands=['statistics'])
async def statistics_msg(message: types.Message):
    try:
        req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
        response = req.json()
        print(response)
        high_price = response['btc_usd']['high']
        low_price = response['btc_usd']['low']
        avg_price = response['btc_usd']['avg']
        vol_trade = response['btc_usd']['vol']
        vol_cur_trade = response['btc_usd']['vol_cur']
        last_price = response['btc_usd']['last']
        updated_cache = response['btc_usd']['updated']
        await bot.send_message(message.chat.id,
            "Статистика за последние 24 часа:\n"
            "Дата: "
            f"{datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
            f"Максимальная цена: {'%.2f' % high_price} USD\n"
            f"Минимальная цена: {'%.2f' % low_price} USD\n"
            f"Средняя цена: {'%.2f' % avg_price} USD\n"
            f"Объем торгов: {'%.2f' % vol_trade}\n"
            f"Объем торгов в валюте: {'%.2f' % vol_cur_trade} USD\n"
            f"Цена последней сделки: {'%.2f' % last_price} USD\n"
            f"Последнее обновление кэша: {'%.2f' % updated_cache}")
    except Exception as ex:
        print(ex)
        await bot.send_message(message.chat.id,
            'Что-то пошло не так, попробуйте позже...')


@dp.message_handler(Text)
async def another_command(message: types.Message):
    await bot.send_message(message.chat.id,
                    'Проверьте введенную команду! Вышла ошибочка...')
