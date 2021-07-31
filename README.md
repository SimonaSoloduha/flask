# flask_project

## запуск проекта:

1. Откройте консоль

2. Перейдите в папку, в которой будет храниться проект 

cd <путь до папки>


2. Склонируйте проект 

git clone https://github.com/SimonaSoloduha/flask


3. перейдите в папку проекта 

cd flask

3. Создайте виртуальное окружение venv

python3 -m venv venv

4. Активируйте виртуальное окружение venv

source venv/bin/activate

5. Установите необходимые пакеты: 

pip3 install -r requirements.txt

(Все используемые библиотеки представлены в файле requirements.txt)

pip3 install flask_sqlalchemy


При необходимости обновите pip 

(Если получите сообщение: 
WARNING: You are using pip version 20.2.3; however, version 21.2.1 is available.
You should consider upgrading via the '..... flask/venv/bin/python3 -m pip install --upgrade pip' command.)


6. Создать БД 

Используя Python REPL создайте базу данных с помощью метода create_all для объекта db. 

>>> from project import db, create_app
>>> db.create_all(app=create_app())

7. Задайте значения FLASK_APP и FLASK_DEBUG 


export FLASK_APP=project

export FLASK_DEBUG=1


8. Запустите проект

flask run 

(Если проект не запускается из-за ошибок в установке пакетов, но при этом вы установили все необходимые пакеты - перезапустите проект выполнив шаги 3, 4, 6)

9. Перейдете по ссыке


http://127.0.0.1:5000/ 

## Описание пользователей 

Есть 2 вида пользователей: 
* С полными правами - SUPERUSER ( roles['superuser'] ) - могут видеть всех пользователей, удалять/редактировать права пользователей 
* С ограниченными - USER ( roles['user'] ) - могут заходить в свой кабинет, не видят вкладку ALL USERS и не имеют доступа к редактированию

Первый пользователь получает права SUPERUSER и изначально только он может сделать SUPERUSER-ром кого-то еще. 
