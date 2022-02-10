# Пульт охранника

Скрипт отображает входы, выходы и информацию по пропускам для банковского хранилища.

### Как установить

Python3 должен быть установлен, затем используйте `pip`

```bash
pip install -r requiremens.txt
```

### Как запустить

Для запуска требуется прописать параметры подключения к базе данных в файле
```
/project/settings.py
```
```Python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'host',
        'PORT': 'port',
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': 'password',
    }
}

```
Затем используйте

```
Python main.py
```
Запустится локальный сервер, сайт будет доступен по адресу: `http://127.0.0.1:8000/`
