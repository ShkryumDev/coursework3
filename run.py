from flask import Flask, jsonify
from logs.api_log import logger_one

from utils import get_posts_all, get_post_by_pk
from app.index.views import index_blueprint
from app.search.search import search_blueprint
from app.user.user import user_blueprint
from app.tag.tag import tag_blueprint

app = Flask(__name__)

app.register_blueprint(index_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(tag_blueprint)


@app.route('/api/posts')
def api_1():
    data = get_posts_all()
    logger_one.info(f'Запрос /api/posts')
    return jsonify(data)


@app.route('/api/posts/<int:post_id>')
def api_2(post_id):
    post = get_post_by_pk(post_id)
    logger_one.info(f'Запрос /api/posts/{post_id}')
    return jsonify(post)


@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(500)
def page_not_found(e):
    return jsonify(error=str(e)), 500


if __name__ == '__main__':
    app.run(debug=True)
