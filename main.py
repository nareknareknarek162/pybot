from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
import requests
from keyboards import *
from constants import *
from generals import *
from translations import *


def translator(text):
    url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"

    querystring = {"langpair": f"{lang[orig_lang]}|{lang[translation_lang]}", "q": text}

    headers = {
        "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com",
        "X-RapidAPI-Key": "395551f690msh46511522fac6803p11b5ecjsn983f78d44fc3"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_response = response.json()
    return json_response["responseData"]["translatedText"]


def search(update, context):
    update.message.reply_text('Что вы хотите найти?', reply_markup=markup3)
    request_type = update.message.text
    return 1


def first_book_response(update, context):
    update.message.reply_text('Как искать книгу?', reply_markup=markup2)
    global search_method
    search_method = update.message.text
    return 2


def second_book_response(update, context):
    update.message.reply_text('Введите название автора или ключевые слова из книги', reply_markup=markup2)
    global request_words
    request_words = update.message.text
    update.message.reply_text('Вот что мне удалось найти')

    return ConversationHandler.END


def search(update, context):
    pass


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    translate_handler = ConversationHandler(
        entry_points=[CommandHandler('translate', translate)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, first_lang_response)],
            2: [MessageHandler(Filters.text & ~Filters.command, second_lang_response)],
            3: [MessageHandler(Filters.text & ~Filters.command, third_lang_response)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    search_handler = ConversationHandler(
        entry_points=[CommandHandler('search', search)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, first_book_response)],
            2: [MessageHandler(Filters.text & ~Filters.command, second_book_response)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(translate_handler)
    dp.add_handler(search_handler)
    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
