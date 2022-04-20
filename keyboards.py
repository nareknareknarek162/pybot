from telegram import ReplyKeyboardMarkup

reply_keyboard = [['/translate', '/help', '/search']]
markup1 = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

languages_choose = [['Русский', 'Английский'], ['Итальянский', 'Немецкий'], ['Датский', 'Испанский']]
markup2 = ReplyKeyboardMarkup(languages_choose, one_time_keyboard=False)

request_type = [['Книга', 'Картина']]
markup3 = ReplyKeyboardMarkup(request_type, one_time_keyboard=False)