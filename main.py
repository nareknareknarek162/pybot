from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
import requests
import json

TOKEN = '5249786699:AAFOz1Rfunpfb0GcuoE-cxkBTqyun_ClkpM'
lang = {
    'Русский': 'ru',
    'Английский': 'en',
    'Италянский': 'it',
    'Немецкий': 'de',
    'Датский': 'da',
    'Испанский': 'es',
}

reply_keyboard = [['/translate', '/help']]
markup1 = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
languages_choose = [['Русский', 'Английский'], ['Итальянский', 'Немецкий'], ['Датский', 'Испанский']]
markup2 = ReplyKeyboardMarkup(languages_choose, one_time_keyboard=False)

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

def start(update, context):
    update.message.reply_text('Привет я бот для поиска книг. Ещё я могу переводить.',
                              reply_markup=markup1)


def help(update, context):
    update.message.reply_text('Функция поиска книг скоро будет добавлена')


def translate(update, context):
    update.message.reply_text('С какого языка производится перевод?', reply_markup=markup2)
    return 1


def first_response(update, context):
    global orig_lang
    orig_lang = update.message.text
    update.message.reply_text("На какой язык необходимо перевести?")
    return 2


def second_response(update, context):
    global translation_lang
    translation_lang = update.message.text
    update.message.reply_text('Напишите текст, который необходимо перевести?')
    return 3


def third_response(update, context):
    text = update.message.text
    update.message.reply_text("Направление перевода осуществляется с")
    update.message.reply_text(f'{orig_lang} ---> {translation_lang}')
    update.message.reply_text(translator(text))
    return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('translate', translate)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, first_response)],
            2: [MessageHandler(Filters.text & ~Filters.command, second_response)],
            3: [MessageHandler(Filters.text & ~Filters.command, third_response)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(conv_handler)
    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
