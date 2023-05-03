from aiogram import Bot, Dispatcher, executor
from auth import token
# парсинг с сайта: https://www.yobit.net/ru/api/


bot = Bot(token=token)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот запущен!')


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)
