from telegram.ext import ConversationHandler
from keyboards import *
import requests
from constants import api_key

def book(update, context):
    update.message.reply_text('Как искать книгу?', reply_markup=book_methods_keyboard)
    context.user_data['search_method'] = update.message.text
    return 1


def first_book_response(update, context):
    update.message.reply_text('Введите необходимую информацию')
    context.user_data['request_words'] = update.message.text
    return 2

def second_book_response(update, context):
    update.message.reply_text('Вот что мне удалось найти')
    if context.user_data['search_method'] == 'По названию':
        return book_by_title(context.user_data['request_words'])
    elif context.user_data['search_method'] == 'По автору':
        pass
    return ConversationHandler.END

def book_by_title(text):
    request = '+'.join(text.split())
    url = f"https://www.googleapis.com/books/v1/volumes?q={request}&maxResults=4&key={api_key}"

    response = requests.get(url)
    json_response = response.json()
    print(response.text)