# Backend приложение для социальной сети - обмен фотографиями

## Описание проекта

Приложение публикует посты, которые состоят из текста и фотографии.  
Дата и время публикации поста фиксируется.  
Публиковать пост может только авторизованный пользователь.  
Редактирует пост только автор. На момент редактирования автор должен быть авторизован.  
Авторизованные пользователи могут комментировать публикации и оставлять реакцию - лайк.  
Авторизованные пользователи могут получать детали каждого опубликованного поста.  
Длина текста поста ограничена - 3000 символов.  
Фотографии могут быть в формате jpg, png, gif и размером до 2 Мб.  
Длина комментария ограничена - 300 символов.  

Создание и авторизация пользователей: создание токенов авторизации производится через  административную панель Django.

В деталях поста, кроме полей поста, отражены:
- список комментариев к посту - comments
- число реакций к посту - likes_count
  
'json'

{  
    "id": 2,  
    "text": "Второй пост",  
    "image": "http://localhost:8000/media/posts/image2.jpg",  
    "created_at": "2025-07-07T10:37:13.176049Z",  
    "comments": [  
        {  
           "author": 2,  
            "text": "Супер!",  
            "created_at": "2025-07-07T11:23:44.411931Z"  
        }  
   ],  
   "likes_count": 1  
}

## Требования

django 5.0.2  
djangorestframework 3.14.0  
pillow 10.2.0  
psycopg2-binary 2.9.9  
geopy 2.4.1  
python-decouple 3.8  
СУБД: PostgreSQL 17


## Быстрый старт

1. Клонирование репозитория

bash  
git clone https://github.com/Burtsev-Sergey/social_network_dp.git  
cd social_network_dp

2. Создание виртуального окружения

bash  
python -m venv venv  
source venv/bin/activate    для Linux/Mac  
venv\Scripts\activate       для Windows  

3. Установка зависимостей

bash  
pip install -r requirements.txt
  

### Настройка переменных окружения

Создайте файл '.env' в корневой директории проекта и добавьте:

DB_PASSWORD=ваш пароль в PostgreSQL  
DB_USER=ваше имя в PostgreSQL  
DB_NAME=имя базы данных - в проекте 'db_dj_diplom'  
DB_HOST=хост - в проекте 'localhost'  
DB_PORT=адрес порта - в проекте '5432'  
DJANGO_KEY=ваш ключ в Django  
Пример конфигурации в файле 'example_config'


### Работа с базой данных

1. Создайте базу данных  
bash  
createdb db_dj_diplom

1. Примените миграции  
bash  
python manage.py migrate

1. Создайте суперпользователя  
bash  
python manage.py createsuperuser


### Запуск приложения

bash  
python manage.py runserver


## Директории и файлы проекта

- social_network_dp/ - папка проекта
- social_network/ — основное приложение/конфигурация Django.
- posts/ — пользовательское приложение Django.
- pictures/ — папка с фотографиями для публикации постов.
- .gitignore — файл с игнорируемыми папками и файлами проекта.
- db_dj_diplom - public - файл со схемой базы данных.
- example_config -  файл с шаблоном для .env файла
- postman_requests_examples - файл с шаблонами запросов для Postman
- requirements.txt — файл с зависимостями проекта.


## Частые ошибки и их решения

- В терминале Windows не распозаются и не выполняются Python команды: 'python -m venv venv' и другие. Вы можете находится в терминале Power Shell - перейдите в терминал cmd, командой 'cmd'.
- Ошибка подключения к БД: Проверьте переменные в .env, доступ пользователя и запущен ли сервер базы данных.
- Миграции не применяются: Попробуйте 'python manage.py makemigrations' и затем 'python manage.py migrate'.


## Контакты и поддержка

- Автор: Сергей
- Эл. почта: sburtsevs@mail.ru
- Telegram: @Sergey_Burcev
- Issues: https://github.com/Burtsev-Sergey/social_network_dp