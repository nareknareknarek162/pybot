def translate(update, context):
    update.message.reply_text('С какого языка производится перевод?', reply_markup=markup2)
    return 1

def first_lang_response(update, context):
    global orig_lang
    orig_lang = update.message.text
    update.message.reply_text("На какой язык необходимо перевести?")
    return 2


def second_lang_response(update, context):
    global translation_lang
    translation_lang = update.message.text
    update.message.reply_text('Напишите текст, который необходимо перевести?')
    return 3


def third_lang_response(update, context):
    text = update.message.text
    update.message.reply_text("Направление перевода осуществляется с", reply_markup=markup1)
    update.message.reply_text(f'{orig_lang} ---> {translation_lang}')
    update.message.reply_text(translator(text))
    return ConversationHandler.END