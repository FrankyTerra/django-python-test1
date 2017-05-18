# django-python-test1

Установка виртуального окружения:

`cd path_to_project_folder/mysite`
`mkdir venv && echo "Virtualenv directory" > venv/README`
`git add venv && echo "/venv/" >> .gitignore && git add -f .gitignore`
`virtualenv --no-site-packages --prompt="(mysite)" venv/mysiteenv`

Активация виртуального окружения:

`source venv/mysiteenv/bin/activate`

Установка необходимых пакетов:

`pip install django`
`pip install django-mptt`
`pip install django-mptt-admin`
`pip install django-bootstrap3`
`pip install django-jquery`

Список пакетов в requirements.txt

`pip freeze > requirements.txt`

Проверка/старт сервера

`python3 manage.py runserver`
