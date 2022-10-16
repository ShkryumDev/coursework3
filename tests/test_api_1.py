# Импортируем данные
from run import app


# Тестируем эндпоинт на возврат списка
def test_posts():
    response = app.test_client().get('/api/posts')
    assert type(response.json) == list


# Тестируем эндпоинт на наличие у элемента нужных ключей
def test_keys():
    response = app.test_client().get('/api/posts')
    list_keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
    test_data = response.json
    test_post = test_data[0]
    assert set(test_post.keys()) == set(list_keys)
