import telebot
from datetime import datetime
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://220727:1234567899@nosql.imvkr4a.mongodb.net/")
db = cluster["telegram_bot"]  
collection = db["messages"] 

bot = telebot.TeleBot('6745684795:AAGB-Z8OeGauM_mIKQP2K7JkQyElnt0L-X4')

def log_message_to_mongodb(text):
    message_document = {
        "text": text,
        "date": datetime.now()
    }
    collection.insert_one(message_document)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    log_message_to_mongodb(message.text)  
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling()
