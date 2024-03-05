import telebot

bot = telebot.TeleBot('6745684795:AAGB-Z8OeGauM_mIKQP2K7JkQyElnt0L-X4')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Strattonbot + {message.text}")

bot.polling()
