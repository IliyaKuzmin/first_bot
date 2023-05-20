import telebot
from extensions import *
from variables import *

bot=telebot.TeleBot(Token)
def show(text,message):
	bot.send_message(message.chat.id,f"Input_Error:{text}")
	raise Input_Error(text)

@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
	text="Чтобы начать работу, введите команду боту в следующем формате:\n <имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>"
	bot.reply_to(message,text)

@bot.message_handler(commands=["values"])
def list(message: telebot.types.Message):
	text="Доступные валюты:"
	for key in NameOfCurrency.keys():
		text="\n".join((text,key, ))
	bot.reply_to(message,text)

@bot.message_handler(content_types=["text"])
def convert(message):
	try:
		base,quote,amount=message.text.split(" ")	
		if float(amount)<0:show("Введенно отрицательное количество переводимой валюты!",message)
		if base not in NameOfCurrency:show("Простите вашей валюты в списке(/values) нет",message)
		if quote not in NameOfCurrency:show("Простите интересующей валюты в списке нет",message)
	except Input_Error:print("Ошибка пользователя")
	else:
		product=NameOfCurrency[base]
		price=NameOfCurrency[quote]
		con=convertor()
		CostOfCurrency=con.get_price(product,price,amount)
		text=f"Цена{amount} {base} в {quote} - {CostOfCurrency}"
		bot.reply_to(message,text)

bot.polling()