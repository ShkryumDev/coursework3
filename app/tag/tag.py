# Импортируем данные
from flask import Blueprint, render_template, request
from utils import search_by_tag

tag_blueprint = Blueprint('tag_blueprint', __name__, template_folder='templates')


# Создаем представление для поиска по тегу
@tag_blueprint.route('/tag')
def tag():
    s = str(request.args.get('s')).lower()
    searched_list = search_by_tag(s)
    return render_template('tag.html', searched_list=searched_list, tag_word=s)
