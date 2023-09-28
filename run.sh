# здесь должено запускаться виртуально окружение питона, после одноременно сервер и тлеграм бот
# python3 -m venv venv
source env/bin/activate
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver & python3 TGBot/main.py