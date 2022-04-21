import requests
from telegram.ext import ConversationHandler
from keyboards import languages_keyboard, start_keyboard
lang = {
    'Русский': 'ru',
    'Английский': 'en',
    'Итальянский': 'it',
    'Немецкий': 'de',
    'Датский': 'da',
    'Испанский': 'es',
}

def translator(text, lang1, lang2):

    url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"

    querystring = {"langpair": f"{lang[lang1]}|{lang[lang2]}", "q": text}

    headers = {
        "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com",
        "X-RapidAPI-Key": "395551f690msh46511522fac6803p11b5ecjsn983f78d44fc3"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_response = response.json()
    return json_response["responseData"]["translatedText"]


def translate(update, context):
    update.message.reply_text('С какого языка производится перевод?', reply_markup=languages_keyboard)
    return 1


def first_lang_response(update, context):
    context.user_data['orig_lang'] = update.message.text
    update.message.reply_text("На какой язык необходимо перевести?")
    return 2


def second_lang_response(update, context):
    context.user_data['translation_lang'] = update.message.text
    update.message.reply_text('Напишите текст, который необходимо перевести?')
    return 3


def third_lang_response(update, context):
    text = update.message.text
    update.message.reply_text("Направление перевода осуществляется с", reply_markup=start_keyboard)
    update.message.reply_text(f'{context.user_data["orig_lang"]} ---> {context.user_data["translation_lang"]}')
    update.message.reply_text(translator(text, context.user_data["orig_lang"], context.user_data["translation_lang"]))
    return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Что поищем?", reply_markup=start_keyboard)
    return ConversationHandler.END