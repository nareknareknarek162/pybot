from keyboards import start_keyboard


def start(update, context):
    update.message.reply_text(
        'Доброго времени суток. Я бот для поиска книг и картин. Чтобы узнать что я могу воспользуйтесь командой /help',
        reply_markup=start_keyboard)
    update.message.reply_text('Что поищем?')


def help(update, context):
    update.message.reply_text('Вы можете искать книги или картины \n'
                              'Для поиска используйте книг используйте команду /book\n '
                              'Для поиска картин используйте команду /painting', reply_markup=start_keyboard)
    update.message.reply_text(
        'Если у вас возникли проблемы с поиском или названием воспользуйтесь переводчиком /translate')
