# Spotify API Music Web Service

Веб-приложение на базе **Django**, реализующее интеграцию со сторонним **Spotify Web API**. Сервис демонстрирует клиент-серверное взаимодействие, аутентификацию по токенам (OAuth / Client Credentials), обработку внешних API-запросов и безопасное управление конфигурацией приложения.

---

## Основной функционал

* **Взаимодействие со Spotify Web API:** отправка HTTP-запросов к внешнему сервису, парсинг и обработка ответов в формате JSON.
* **Безопасная конфигурация:** изоляция чувствительных данных (секретные ключи Django, Client ID и Client Secret Spotify) в переменных окружения через '.env'.
* **Архитектурный фундамент:** модульная структура Django с разделением логики запросов, настроек и шаблонов.

---

## Стек технологий

* **Язык:** Python 3.14
* **Фреймворк:** Django
* **Безопасность и окружение:** 'python-dotenv'
* **Контроль версий:** Git, GitHub

---

## Быстрый старт и локальный запуск

1. **Клонирование репозитория:**
   ```bash
   git clone [https://github.com/ag00ny/Spotify-API.git](https://github.com/ag00ny/Spotify-API.git)
   cd Spotify-API
   ```

2. **Настройка виртуального окружения:**
   * **Windows (PowerShell):**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   * **macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Установка зависимостей:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройка переменных окружения (`.env`):**
   * Создайте файл конфигурации:
     ```bash
     # Windows
     copy .env.example .env

     # Linux / macOS
     cp .env.example .env
     ```
   * Откройте созданный '.env' и укажите актуальные данные:
     '''
     SECRET_KEY=секретный_ключ_django
     DEBUG=True

     SPOTIFY_CLIENT_ID=spotify_client_id
     SPOTIFY_CLIENT_SECRET=spotify_client_secret
     '''
   > API-ключи Spotify можно получить в [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).

5. **Применение миграций и запуск сервера:**
   '''bash
   python manage.py migrate
   python manage.py runserver
   '''
   Сервис запустится локально по адресу: 'http://127.0.0.1:8000/'

---

## Структура проекта


├── music/               # Основное Django-приложение (логика интеграции и вьюхи)
├── settings/            # Конфигурационные файлы проекта (settings.py, urls.py, wsgi.py)
├── .env.example         # Публичный шаблон переменных окружения
├── .gitignore           # Исключение кэша, виртуального окружения и секретов
├── manage.py            # Точка входа для управления проектом
└── requirements.txt     # Список зависимостей Python
