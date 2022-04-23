from telegram.ext import ConversationHandler
from keyboards import *
import requests
from constants import api_key


def book(update, context):
    update.message.reply_text('Как искать книгу?', reply_markup=book_methods_keyboard)
    return 1


def first_book_response(update, context):
    context.user_data['search_method'] = update.message.text
    if context.user_data['search_method'] == 'По названию':
        update.message.reply_text('Введите название книги или ключевые слова')
    elif context.user_data['search_method'] == 'По автору':
        update.message.reply_text('Введите автора книги затем ключевые слова из книги на разных строчках')

    return 2


def second_book_response(update, context):
    context.user_data['request_words'] = update.message.text
    update.message.reply_text('Вот что мне удалось найти', reply_markup=start_keyboard)
    if context.user_data['search_method'] == 'По названию':
        info = book_by_title(context.user_data['request_words'])
    elif context.user_data['search_method'] == 'По автору':
        info = book_by_author(context.user_data['request_words'])
    update.message.reply_text(f"{info[0]}\n Автор - {' '.join(info[1])} \n Описание: {info[2]}")
    if info[3]:
        update.message.reply_text(info[3])
    return ConversationHandler.END


def book_by_title(text):
    request = '+'.join(text.split())
    url = f"https://www.googleapis.com/books/v1/volumes?q={request}&maxResults=4&key={api_key}"

    response = requests.get(url)
    json_response = response.json()

    book_params = list()
    title = json_response["items"][0]["volumeInfo"]["title"]
    author = json_response["items"][0]["volumeInfo"]["authors"]
    book_params.append(title)
    book_params.append(author)
    if "description" in json_response:
        description = json_response["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
    else:
        description = 'отсутсвует'
    book_params.append(description)
    if "imageLinks" in json_response["items"][0]["volumeInfo"]:
        pic = json_response["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
    else:
        pic = False
    book_params.append(pic)

    return book_params


def book_by_author(text):
    request = '+'.join(text.split('\n')[1].split())
    author = '+'.join(text.split('\n')[0].split())
    url = f"https://www.googleapis.com/books/v1/volumes?q={request}+inauthor:{author}&maxResults=4&key={api_key}"

    response = requests.get(url)
    json_response = response.json()

    book_params = list()
    title = json_response["items"][0]["volumeInfo"]["title"]
    author = json_response["items"][0]["volumeInfo"]["authors"]
    book_params.append(title)
    book_params.append(author)
    if "description" in json_response:
        description = json_response["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
    else:
        description = 'Описание отсутсвует'
    book_params.append(description)
    if "imageLinks" in json_response["items"][0]["volumeInfo"]:
        pic = json_response["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
    else:
        pic = False
    book_params.append(pic)

    return book_params
