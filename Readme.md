### Как запустить проект

1. Создайте файл .env в корне проекта. Используйте файл .env_example как образец.

2. Очистите старые контейнеры (опционально). Если вы ранее запускали проект и хотите начать с чистого состояния,
   выполните:
    - docker-compose down -v

3. Запустите проект. Для его запуска, выполните команду ниже. Тесты запустятся автоматически в отдельном контейнере
    - docker-compose up --build

4. После успешного запуска функционал проекта будет доступен по адресу:
   http://localhost:7000/

