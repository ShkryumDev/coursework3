# Импортируем данные
import json
from config import path_data, path_comments
from json import JSONDecodeError


# Функция, которая возвращает все посты
def get_posts_all():
    try:
        with open(path_data, 'r', encoding='UTF-8') as f:
            our_list = json.load(f)
            return our_list
    except FileNotFoundError:
        print('Файл data.json не найден')
    except JSONDecodeError:
        print('Файл data.json не удается преобразовать')


# Функция, которая возвращает посты определенного пользователя
def get_posts_by_user(user_name):
    users_posts = []
    data = get_posts_all()
    for i in data:
        if i['poster_name'] == user_name:
            users_posts.append(i)
    if not users_posts:
        raise ValueError('Такого пользователя не существует. Ошибка 500')
    return users_posts


# Функция, которая возвращает комментарии определенного пользователя
def get_comments_by_post_id(pk):
    list_comments = []
    with open(path_comments, 'r', encoding='UTF-8') as f:
        all_comments = json.load(f)
    for comments in all_comments:
        if comments['post_id'] == pk:
            list_comments.append(comments)
    return list_comments


# Функция, которая возвращает список постов по ключевому слову
def search_for_posts(query):
    data = get_posts_all()
    searched_posts = []
    for i in data:
        if query.lower() in i['content'].lower():
            searched_posts.append(i)
    return searched_posts


# Функция, которая возвращает один пост по его идентификатору
def get_post_by_pk(pk):
    data = get_posts_all()
    for i in data:
        if i['pk'] == pk:
            post = i
            return post


# Функция, которая возвращает пост по тегу
def search_by_tag(tag_word):
    data = get_posts_all()
    searched_posts = []
    for i in data:
        if tag_word.lower() in i['tag'].lower():
            searched_posts.append(i)
    return searched_posts
