import telebot

token = "5613541473:AAHJ4A2OadP-yScm6RRi-ULghTozlJ8Vd8s"

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    if "Costa" in message.text:
        bot.send_message(message.chat.id, "hi my man!")
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling(non_stop=True)
