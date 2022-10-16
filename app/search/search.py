# Импортируем данные
from flask import Blueprint, render_template, request
from utils import search_for_posts

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


# Создаем представление для поиска по маршруту 'search/?s='
@search_blueprint.route('/search')
def search_page():
    s = str(request.args.get('s')).lower()
    searched_list = search_for_posts(s)
    count_posts = len(searched_list)
    return render_template('search.html', searched_list=searched_list, for_search=s, count=count_posts)
