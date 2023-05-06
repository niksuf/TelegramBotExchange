from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb = ReplyKeyboardMarkup(resize_keyboard=True)
price_button = KeyboardButton('Цена')
statistics_button = KeyboardButton('Статистика')
help_button = KeyboardButton('Помощь')
kb.add(price_button).insert(statistics_button).insert(help_button)
