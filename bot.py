import os
import logging
from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from flask import Flask, request

# إعدادات البوت
TOKEN = '998371661:AAEfGr2Ib7SDdX2D_fx-DtyHDpy1P93fsX8'
WEBHOOK_URL = 'https://your-vercel-app-url'

app = Flask(__name__)
bot = Bot(token=TOKEN)

# إعداد المعالجات
def start(update, context):
    update.message.reply_text("مرحبًا! أنا بوت يعمل على Vercel.")

def handle_message(update, context):
    update.message.reply_text(f"أنت قلت: {update.message.text}")

# إعدادات الـ Dispatcher
dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == "POST":
        json_str = request.get_data().decode("UTF-8")
        update = telegram.Update.de_json(json_str, bot)
        dispatcher.process_update(update)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
