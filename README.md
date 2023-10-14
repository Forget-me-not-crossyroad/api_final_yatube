# Проект «API для Yatube»
Проект программной части API для сервиса видеохостинга.
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Forget-me-not-crossyroad/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

Получить документацию API проекта при запущенном локально проекте:

```
http://127.0.0.1:8000/redoc/
```

Скачать и установить Postman для изучения API проекта:

```
https://www.postman.com/
```

Проверить работоспособность API проекта (GET-запрос):

```
GET http://127.0.0.1:8000/api/v1
```

