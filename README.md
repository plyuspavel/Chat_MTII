# Общие слова
Основной код лежит в папке **Site**. В ней в файле app.py содержится сам код и логика работы чата. В папке templates лежат шаблоны страничек чата.  
Остальные файлы и папки нужны для конфигурации и сборки Docker образа.

# Сборка и запуск проекта
* Скачайте файлы репозитория к себе на сервер. 
* Чтобы запустить докер нужно два образа: образ бд postgres и образ веб приложения (сайта).
Чтобы собрать образ сайта нужен файл Dockerfile в той же папке. 
**Из папки Site выполните команду *docker build -t flsk .*** (точка на конце нужна) - мы начали сборку образа.
Теперь в облаке docker'a будет образ flsk.
* Теперь нам нужен образ бд postgres. 
**Выполните команду *sudo docker pull postgres***. У нас появился уже образ postgres. Имеются 2 образа из 3 необходимыъ
* Третий образ - третий это первичная настройка бд, т.е. создание базы данных, пользователя админ, создание трех таблиц для чата и регистрации. Это делает скрипт preinst.py.
**Из папки Preinst выполните команду *docker build -t preinst .***
* Nеперь у нас есть три образа на машине в docker'e.
**Из корневой папки выполните команду *docker-compose up***
Эта команда достанет три образа, скомпанует, запустит сервер с бд в докере, запустит сервер с сайтом, перенаправит порты, запустит скрипт начальный установки таблиц preinst и будет работать. Но для ее работы нужы файлы docker-compose.yml и init.sql. init нужен для postgres образа: он создает пользователя и базу данных, а preinst создает таблицы.
