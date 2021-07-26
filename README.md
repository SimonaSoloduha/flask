# flask_project

## запуск проета:

Скачать проект на свой компьютер


Консоль: 
cd <путь до проекта>
Создать и активировать венв

source venv/bin/activate

# Установить пакеты: 

pip install flask 
pip install flask flask-sqlalchemy flask-login 
pip3 install flask_sqlalchemy 
pip3 install flask_security

(Все используемые библиотеки представлены в файле requirements.txt)

# Создать БД 
Используя Python REPL создаем базу данных, используя метод create_all для объекта db. 

Убедитесь, что вы все еще находитесь в виртуальной среде и в каталоге flask_auth_app: 
* from project import db, create_app
* db.create_all(app=create_app())

# Задать значения FLASK_APP и FLASK_DEBUG 

* 		export FLASK_APP=flask
* 		export FLASK_DEBUG=1

# Запустить проект 
flask run 
