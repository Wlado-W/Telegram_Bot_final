import telebot
import config
from extensions import *

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    response = 'Это бот умеет конвертировать валюты используя онлайн информацию о ценах валют.\nЧтоб использовать бота введите команду /value в формате:\n/value <сумма> <ваша_валюта> <желаемая_валюта>\nНапример: /value 1000 USD RUB'
    bot.send_message(message.chat.id,response)

@bot.message_handler(commands=['value'])
def handle_value(message):
    try:
        print(f"message.text: {message.text}")
        values = message.text.split()
        if len(values) !=4:
            raise Exception('Неверный формат команды')
        amount = float(values[1])
        base_currency = str(values[2].upper())
        target_currency = str(values[3].upper())
        print(f"amount: {amount}, base_currency: {base_currency}, target_currency: {target_currency}")
        converter = CurrencyConverter(config.API_KEY)
        result = converter.convert(base_currency,target_currency,amount)
        response = f'{amount} {base_currency} = {result:.2f} {target_currency}'

    except Exception as e:
        response = str(e)

    bot.send_message(message.chat.id, response)

bot.polling(none_stop=True)