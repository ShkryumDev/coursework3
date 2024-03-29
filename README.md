# Курс 3. Курсовая

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bb8c2d8f-7405-4704-9ba3-0770d8390c54/Untitled.png)

**Привет, с вами Джони Кэтсвилл,** и сегодня мы будем делать свой Instagram 
с едой, котами и еще раз едой! 

Эта курсовая потребует знания HTML, Flask, Jinja  и, конечно же, Python.

![2022-04-01 14.53.48.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/535dde70-367d-4cc4-821d-5a826159f876/2022-04-01_14.53.48.gif)

<aside>
💡 ВАЖНО! Сначала **изучить материалы всех пройденных уроков**, а только потом приступать к выполнению курсовой работы.

</aside>

# Описание проекта

Нажмите на пункт, чтобы раскрыть его

- **Лента**
    
    Список всех постов. У каждого выводится автор, укороченный до 50 символов текст, количество просмотров , ссылка, которая ведет на пост. 
    
    В шапочке ссылка флажок – ссылка на закладки.
    
    https://www.figma.com/embed?embed_host=notion&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FSNcwz5Ri8eHj0dF2QUiGyq%2Fpython_backend_008_projects%3Fnode-id%3D79%253A63
    
- **Подробный пост**
    
    
    Страничка с подробной информацией про пост. 
    
    Фото, текст поста и карточка автора берутся из данных поста.
    
    Комментарии берутся из файла с комментариями.
    
    Ссылка "назад" ведет на главную
    
    https://www.figma.com/embed?embed_host=notion&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FSNcwz5Ri8eHj0dF2QUiGyq%2Fpython_backend_008_projects%3Fnode-id%3D79%253A491
    
- **Поиск**
    
    
    Форма поиска, отправляется по нажатию на Enter. После нее – результаты поиска. 
    
    https://www.figma.com/embed?embed_host=notion&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FSNcwz5Ri8eHj0dF2QUiGyq%2Fpython_backend_008_projects%3Fnode-id%3D79%253A656
    
- **Все посты пользователя (версия со звездочкой)**
    
    Посты выбранного пользователя по порядку
    
    Кнопка "назад" ведет на главную
    
    https://www.figma.com/embed?embed_host=notion&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FSNcwz5Ri8eHj0dF2QUiGyq%2Fpython_backend_008_projects%3Fnode-id%3D79%253A608
    
- **Посты по тегу (версия со звездочкой)**
    
    Когда мы нажимаем на хештег в коде, то переходим на страничку со всеми постами, где такой же хештег встречается.  Кнопка "назад" ведет на главную.
    
    https://www.figma.com/embed?embed_host=notion&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FSNcwz5Ri8eHj0dF2QUiGyq%2Fpython_backend_008_projects%3Fnode-id%3D79%253A549
    
- **Закладки (версия со звездочкой)**
    
    Страничка, на которую попадают отмеченные посты. 
    
    Со странички можно удалять посты.
    
    Кнопка "назад" ведет на главную.
    
    https://www.figma.com/embed?embed_host=notion&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FSNcwz5Ri8eHj0dF2QUiGyq%2Fpython_backend_008_projects%3Fnode-id%3D79%253A323
    

# Основная часть

### Шаг подготовительный

Скопируйте репозиторий со всеми данными: 

https://github.com/skypro-008/coursework2_source

Вы найдете в нем список постов, картинки, шаблоны HTML и CSS-стили.

Переложите шаблоны в папку `templates`.

Переложите стили и картинки в папку `static`.

Обратите внимание: данные хранятся раздельно. Посты вместе с информацией об авторе и его аватаркой хранятся в файле `posts.json`, а комментарии хранятся в файле `comments.json`. Также создан файл `bookmarks.json`, где можно будет хранить закладки.

У каждого поста указаны:

`poster_name` — имя/юзернейм автора поста,

`poster_avatar` — аватарка автора поста,

`pic` — картинка поста,

`content` — текст поста,

`views_count` — количество просмотров,

`likes_count` — количество лайков,

`pk` — id или номер поста.

Обратите внимание, количество комментариев не указано!

У каждого комментария указаны:

`post_id` – к какому посту этот комментарий

`commenter_name` – имя комментатора

`comment` – текст комментария

`pk` – идентификатор (номер) комментарий

### Шаг 0 – подготовьте необходимые функции

Прежде, чем приступать к написанию Flask-приложения, полезно разработать функции, для работы с данными и сложить их в отдельном файле, например, `utils.py.` Например:

`get_posts_all()` – возвращает посты

`get_posts_by_user(user_name)` – возвращает посты определенного пользователя. Функция должна вызывать ошибку `ValueError` если такого пользователя нет и пустой список, если у пользователя нет постов.

`get_comments_by_post_id(post_id)` – возвращает комментарии определенного поста. Функция должна вызывать ошибку `ValueError` если такого поста нет и пустой список, если у поста нет комментов. 

`search_for_posts(query)` – возвращает список постов по ключевому слову

`get_post_by_pk(pk)` – возвращает один пост по его идентификатору. 

Напишите к каждой функции юнит тесты, расположите тесты в отдельной папке `/tests`.

Организуйте тесты в виде классов или функций, на ваше усмотрение.

### Шаг 1 – реализуйте ленту

Создайте представление для всех постов, это должна быть главная страница.

`GET` `/` 

В нем должно показываться столько постов, сколько есть. Найдите и используйте подходящий шаблон. Замените в каждом шаблоне пути к файлу стилей и картинкам. Замените их на /`static/img` и `/static/css` соответственно!

### Шаг 2 – реализуйте просмотр поста

Создайте представление для одного поста 

`GET /posts/<postid>` 

Получите комментарии из файла `comments.json`, у которых соответствующий `postid`.

Выведите комментарии к посту.

Не обрабатывайте теги – вы сделаете это в одном из следующих шагов.

### Шаг 3 – реализуйте поиск

Создайте представление для поиска по маршруту `GET /search/?s=...` 

В нем должно отображаться 10 постов, если есть. 

Поиск должен выполняться по вхождению ключевого слова в текст поста. Регистрозависимость на ваше усмотрение. 

Найдите и используйте подходящий шаблон для вывода результатов. 

### Шаг 4 – Реализуйте вывод по пользователю

Создайте представление с выводом постов конкретного пользователя `GET /users/<username>`. Выведите те посты у которых poster name соответствует `username` из запроса. Используйте шаблон `user-feed`

### Шаг 5 – Добавьте обработчики ошибок

Добавьте обработчик запросов к несуществующим страницам, например `/meow` и верните в этом случае статус-код 404.

Добавьте обработчик ошибок, возникших на стороне сервера (ошибка 500, Internal Server Error ) и верните в этом случае статус-код 500.

### Шаг 6 – сделайте 2 API - эндпоинта

Создайте представление, которое обрабатывает запрос `GET /api/posts` и возвращает полный список постов в виде JSON-списка.

Создайте представление, которое обрабатывает запрос `GET /api/posts/<post_id>` и возвращает один пост в виде JSON-словаря.

### Шаг 7 – залогируйте обращения к эндпоинтам API

Используйте стандартный logging, логи должны храниться в папке logs в файле `api.log` . Формат логов должен быть таким:

```python
%(asctime)s [%(levelname)s] %(message)s
```

Пример:

```python
2022-03-18 18:48:56 [INFO]Запрос /api/posts
2022-03-18 18:48:57 [INFO]Запрос /api/posts
2022-03-18 18:48:58 [INFO]Запрос /api/posts/2
2022-03-18 18:48:59 [INFO]Запрос /api/posts/3

```

### Шаг 8 – добавьте тест на API

Протестируйте эндпоинт `GET /api/posts` , проверьте, что

- возвращается список
- у элементов есть нужные ключи

Не проверяйте количество элементов в списке, так как оно может меняться

Протестируйте эндпоинт `GET /api/posts/<post_id>` , проверьте, что

- возвращается словарь
- у элемента есть нужные ключи

Не проверяйте данные в полученном словаре, это не обязательно.

### Шаг 8 - опубликуйте проект

**Выложите свой проект на GitHub**

- создайте удаленный репозиторий
- добавьте нужные файлы в `.gitignore`
- оформите README
- сделайте пуш

Сдайте задание со ссылкой на репозиторий. Готово, вы превосходны!

### Подсказка:

Чтобы вывести в шаблоне строку, которая содержит HTML-теги, используйте `{{ content|safe }}` – это специальный синтаксис, который разрешает выводить теги "живые" теги, а не их текстовое представление.

# Задание со звездочкой

### Шаг 1 – Реализуйте переход по тегам

Вернитесь к представлению, которое выводит пост. В тексте поста отыщите слова, выберите такие, которые начинаются с `#` и превратите их ссылки по принципу `#food` >>> `<a href="/tag/food">#food</a>`

Создайте представление для `/tag/<tagname>.` В списке постов отыщите такие, которые содержат тег, начинающийся с решетки. Выведите их в соответствующем шаблоне

### Шаг 2 – добавьте посты в закладки.

Создайте представление с добавлением в закладки по маршруту `bookmarks/add/postid`.

Храните закладки в файле `bookmarks.json`. 

После добавления переадресуйте на главную страницу. (`/`)

Для переадресации (редиректа) используйте 

```python
#  Для переадресации (редиректа) используйте 
return redirect("адрес", code = 302) 
```

Создайте представление с удалением из закладок по маршруту `bookmarks/remove/postid`.

После удаления закладки переадресовывайте на главную страницу (`/`)

### Шаг 3 – выведите закладки

Добавьте представление `/bookmarks` для просмотра всех закладок — покажите там все посты, которые добавлены в закладки. Данные возьмите из `bookmarks.json`.
