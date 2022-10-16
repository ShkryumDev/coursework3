# Импортируем данные
from flask import Flask, jsonify
from logs.api_log import logger_one

from utils import get_posts_all, get_post_by_pk
from app.index.views import index_blueprint
from app.search.search import search_blueprint
from app.user.user import user_blueprint
from app.tag.tag import tag_blueprint

app = Flask(__name__)
app.config.from_pyfile('config.py')
path_data = app.config.get('path_data')
path_comments = app.config.get('path_comments')


# Регистрируем блюпринты
app.register_blueprint(index_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(tag_blueprint)


# Представление, которое обрабатывает запрос и возвращает полный список постов в виде JSON
@app.route('/api/posts')
def api_1():
    data = get_posts_all()
    logger_one.info(f'Запрос /api/posts')
    return jsonify(data)


# Представление, которое обрабатывает запрос и возвращает один пост в виде JSON
@app.route('/api/posts/<int:post_id>')
def api_2(post_id):
    post = get_post_by_pk(post_id)
    logger_one.info(f'Запрос /api/posts/{post_id}')
    return jsonify(post)


# Создаем обработчик запросов к несуществующим страницам
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404


# Создаем обработчик ошибок, возникших на стороне сервера
@app.errorhandler(500)
def page_not_found(e):
    return jsonify(error=str(e)), 500


if __name__ == '__main__':
    app.run(debug=True)
