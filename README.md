# API_YamDB

REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке.

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Произведению может быть присвоен жанр. Новые жанры может создавать только администратор.
Читатели оставляют к произведениям текстовые отзывы и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти).
Из множества оценок автоматически высчитывается средняя оценка произведения.

Аутентификация по JWT-токену

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON

Cоздан в команде из трёх человек с использованим Git в рамках учебного курса Яндекс.Практикум.

## Стек технологий
- проект написан на Python с использованием Django REST Framework
- библиотека Simple JWT - работа с JWT-токеном
- библиотека django-filter - фильтрация запросов
- база данных - PostgreSQL
- система управления версиями - git

## Как запустить проект (Docker):

#### 1) Сборка и запуск контейнера
```bash
docker-compose up -d --build 
```
#### 2) Выполнение миграций
```bash
docker-compose run web python manage.py migrate --no-input
```

### 3) Создание суперпользователя Django
```bash
docker-compose run web python manage.py createsuperuser
```
### 4) Сборка статики
```bash
docker-compose run web python manage.py collectstatic --no-input 
```

### 5) Загрузка тестовых данных:
```bash
docker-compose run web python manage.py loaddata fixture.json
```

Полная документация ([redoc.yaml](https://github.com/leks20/yamdb/blob/master/static/redoc.yaml)) доступна по адресу http://127.0.0.1:8000/redoc/

С помощью команды *pytest* вы можете запустить тесты и проверить работу модулей

## Алгоритм регистрации пользователей
- Пользователь отправляет запрос с параметрами *email* и *username* на */auth/email/*.
- YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес *email* .
- Пользователь отправляет запрос с параметрами *email* и *confirmation_code* на */auth/token/*, в ответе на запрос ему приходит token (JWT-токен).

## Ресурсы API YaMDb

- Ресурс AUTH: аутентификация.
- Ресурс USERS: пользователи.
- Ресурс TITLES: произведения, к которым пишут отзывы (определённый фильм, книга или песня).
- Ресурс CATEGORIES: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- Ресурс GENRES: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- Ресурс REVIEWS: отзывы на произведения. Отзыв привязан к определённому произведению.
- Ресурс COMMENTS: комментарии к отзывам. Комментарий привязан к определённому отзыву.
______________________________________________________________________
### Пример http-запроса (POST) для создания нового комментария к отзыву:
```
url = 'http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/'
data = {'text': 'Your comment'}
headers = {'Authorization': 'Bearer your_token'}
request = requests.post(url, data=data, headers=headers)
```
### Ответ API_YamDB:
```
Статус- код 200

{
 "id": 0,
 "text": "string",
 "author": "string",
 "pub_date": "2020-08-20T14:15:22Z"
}
```

###Бейдж
https://github.com/drag0nfather/yamdb_final/workflows/Yamdb_final_workflow/badge.svg