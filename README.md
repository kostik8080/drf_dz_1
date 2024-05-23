# Описание для запуска проекта в Docker

## Шаг 1: Установка Docker и Docker Compose
___

* :white_check_mark: Убедитесь, что Docker установлен на вашей системе. Если Docker не установлен, следуйте
инструкциям для вашей операционной системы, чтобы установить Docker. 
[скачать Docker Desktop](https://www.docker.com/products/docker-desktop/)
* :white_check_mark: Убедитесь, что Docker Compose установлен на вашей системе. Если Docker Compose не установлен, 
следуйте инструкциям для вашей операционной системы, чтобы установить Docker Compose.
___

## Шаг 2: Клонирование репозитория
___

* :white_check_mark: Склонируйте репозиторий проекта на вашу локальную машину.
___

## Шаг 3: Настройка файла .env
___

* :white_check_mark: Создайте файл .env в корневой директории проекта.
* :white_check_mark: В файле .env укажите необходимые переменные окружения, такие как порты, пароли, 
и другие настройки, которые требуются для вашего проекта.
___

## Шаг 4: Запуск Docker контейнеров
___

* :white_check_mark: Откройте терминал и перейдите в корневую директорию проекта.
* :white_check_mark: Запустите команду <mark>docker-compose build</mark>, <mark>docker-compose up</mark>, или 
можно воспользоваться одной командой <mark>docker-compose up -d --build</mark> для запуска Docker контейнеров, 
описанных в файле docker-compose.yml.
* :white_check_mark: Дождитесь, пока все контейнеры успешно запустятся.
___

## Шаг 5: Проверка работоспособности
___

* :white_check_mark: Откройте веб-браузер и перейдите по указанному вами адресу и порту, чтобы убедиться, 
что ваше приложение работает должным образом.
___

## Шаг 6: Остановка контейнеров
___

* :white_check_mark: Чтобы остановить контейнеры, откройте терминал и выполните команду docker-compose down.
___
