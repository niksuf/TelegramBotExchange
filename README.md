# Телеграм-бот парсер стоимости и статистики BTC
## Описание проекта

Данный телеграм-бот является парсером с сайта ```https://www.yobit.net/```. Парсинг происходит посредством открытого API данной биржи. Бот может показать текущую 
стоимость покупки/продажи BTC в USD, а так же статистику за последние 24 часа. Структура ```*.json``` файла приведена ниже.

![json_format](https://github.com/niksuf/TelegramBotVPS/blob/master/img/json_format.png)

## Команды бота

```/start``` - запуск бота;\
```/help``` - список команд бота;\
```/price``` - цена покупки/продажи BTC в USD;\
```/statistics``` - статистика за последние 24 часа.

## Запуск бота

1. Скачать репозиторий к себе на компьютер при помощи команды:
```git clone https://github.com/niksuf/ArduinoFFT```
2. Зарегестрировать нового бота в телеграм при помощи бота ```https://t.me/BotFather```.
3. В файл ```auth.py``` прописать токен бота.
4. Запустить ```main.py```.
