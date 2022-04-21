from keyboards import *
def start(update, context):
    update.message.reply_text('Привет я бот для поиска книг. Ещё я могу переводить.',
                              reply_markup=markup1)

def help(update, context):
    update.message.reply_text('Доброго времени суток. Это бот для поиска художественных произведений')
    update.message.reply_text('Вы можете искать книги или картины. Для поиска используйте команду /search')
    update.message.reply_text(
        'Если у вас возникли проблемы с поиском или названием воспользуйтесь переводчиком /translate')
