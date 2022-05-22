Проект выполнен в рамках тестового задания компании РАНКС.

Для запуска проекта необходимо использователь Docker (https://www.docker.com/get-started/)

Когда Docker будет успешно установлен необходимо, находясь в корневой директории (simple_stripe), 
воспользоваться командой docker-compose build для создания образа проекта.

После сборки образа воспользоваться командой docker-compose up.
Запустятся 2 контенера: stripe_proj - контейнер с джанго проектом и simple_stripe_pg_db_1 - контейнер с PostgreSQL.
Сервер будет автоматически запущен, для проверки можно перейти на url http://localhost:8000/admin (http://0.0.0.0:8000/admin).
Если панель администратора открывается - значит проект успешно запущен.

Изначально база даных пустая, для заполнения тестовыми данными необходимо выполнить команду:
docker exec -it stripe_proj python /usr/src/simple_stripe/manage.py populating_database

populating_database.py - скрипт заполняющий БД 9 записями Item.

Для создания суперпользователя выполнить команду: 
docker exec -it stripe_proj python /usr/src/simple_stripe/manage.py createsuperuser
после чего заполнить username и password.

После чего можно отправлять GET запросы на следующие url:

http://0.0.0.0:8000/buy/{id}, где id - id объекта в БД (от 1 до 9).
В результате выполнения запроса будет Stripe Session Id для оплаты выбранного Item.

http://0.0.0.0:8000/item/{id}, где id - id объекта в БД (от 1 до 9).
C помощью данного запроса можно получить HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. 
По нажатию на кнопку Buy происходит запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe 
происходит редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id).
