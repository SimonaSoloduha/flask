# flask_project

## запуск проекта:

1. Скачать проект на свой компьютер

2. Перейти в консоль для запуска

cd <путь до проекта>

3. Создать и активировать venv
python3 -m venv
source venv/bin/activate

3. Установить пакеты: 

pip3 install -r requirements.txt

(Все используемые библиотеки представлены в файле requirements.txt)

4. Создать БД 
Используя Python REPL создаем базу данных, используя метод create_all для объекта db. 

Убедитесь, что вы все еще находитесь в виртуальной среде и в каталоге flask_auth_app: 
* from project import db, create_app
* db.create_all(app=create_app())

5. Задать значения FLASK_APP и FLASK_DEBUG 

* 		export FLASK_APP=flask
* 		export FLASK_DEBUG=1

6. Запустить проект 
flask run 


## Описание пользователей 

Есть 2 вида пользователей: 
* С полными правами - SUPERUSER ( roles['superuser'] ) - могут видеть всех пользователей, удалять/редактировать права пользователей 
* С ограниченными - USER ( roles['user'] ) - могут заходить в свой кабинет, не видят вкладку ALL USERS и не имеют доступа к редактированию

Первый пользователь получает права SUPERUSER и изначально только он может сделать SUPERUSER-ром кого-то еще. 
