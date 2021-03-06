from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from translator import *
from constants import TOKEN
from general_functions import *
from book_fuctions import *
from picture_functions import *


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    translate_handler = ConversationHandler(
        entry_points=[CommandHandler('translate', translate)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, first_lang_response, pass_user_data=True)],
            2: [MessageHandler(Filters.text & ~Filters.command, second_lang_response, pass_user_data=True)],
            3: [MessageHandler(Filters.text & ~Filters.command, third_lang_response, pass_user_data=True)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    book_handler = ConversationHandler(
        entry_points=[CommandHandler('book', book)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, first_book_response, pass_user_data=True)],
            2: [MessageHandler(Filters.text & ~Filters.command, second_book_response, pass_user_data=True)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("painting", painting))
    dp.add_handler(translate_handler)
    dp.add_handler(book_handler)
    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
