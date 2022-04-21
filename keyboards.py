from telegram import ReplyKeyboardMarkup

reply_keyboard = [['/translate', '/help'], ['/book', '/painting']]
start_keyboard = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

languages_choose = [['Русский', 'Английский'], ['Итальянский', 'Немецкий'], ['Датский', 'Испанский']]
languages_keyboard = ReplyKeyboardMarkup(languages_choose, one_time_keyboard=False)

book_methods = [['По названию','По автору']]
book_methods_keyboard = ReplyKeyboardMarkup(book_methods, one_time_keyboard=False)
