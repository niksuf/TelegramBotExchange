import requests
from datetime import datetime
import telebot
from auth_data import token
# парсинг с сайта: https://www.yobit.net/ru/api/


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_msg(message):
        bot.send_message(message.chat.id, 'Привет! Напиши /help, чтобы узнать функции бота!')

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == '/price':
            try:
                req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
                response = req.json()
                print(response)
                sell_price = response['btc_usd']['sell']
                buy_price = response['btc_usd']['buy']
                bot.send_message(
                    message.chat.id,
                    "Дата: "
                    f"{datetime.now().strftime('%d.%m.%Y %H:%M')}\nЦена продажи 1 BTC: {'%.2f' % sell_price} USD\n"
                    f"Цена покупки 1 BTC: {'%.2f' % buy_price} USD")
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    'Что-то пошло не так, попробуйте позже...')
        elif message.text.lower() == '/statistics':
            try:
                req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
                response = req.json()
                print(response)
                high_price = response['btc_usd']['high']
                low_price = response['btc_usd']['low']
                bot.send_message(
                    message.chat.id,
                    "Статистика за последние 24 часа:\n"
                    "Дата: "
                    f"{datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
                    f"Максимальная цена: {'%.2f' % high_price} USD\n"
                    f"Минимальная цена: {'%.2f' % low_price} USD")
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    'Что-то пошло не так, попробуйте позже...')
        elif message.text.lower() == '/help':
            bot.send_message(
                message.chat.id,
                "Функции бота:\n"
                "/price - цена покупки и продажи BTC\n"
                "/statistics - статистика за последние 24 часа")
        else:
            bot.send_message(
                message.chat.id,
                'Проверьте введенную команду! Вышла ошибочка...')

    bot.polling()


if __name__ == '__main__':
    telegram_bot(token)
