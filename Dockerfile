# Используйте базовый образ Python
FROM python:3.8

# Установите рабочую директорию в контейнере
WORKDIR /app

# Скопируйте файл requirements.txt в контейнер
COPY requirements.txt .

# Установите зависимости Python
RUN pip install -r requirements.txt

# Копирует все файлы из нашего локального проекта в контейнер
ADD . /app

# Запустите команду для запуска Django-приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Запускает команду makemigrations для создания файлов миграции на основе изменений в моделях
RUN python manage.py makemigrations