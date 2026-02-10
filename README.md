# URL Shortener

Простой сервис для сокращения ссылок с использованием FastAPI и SQLite.  

---
## Установка

1. **Клонируем репозиторий**

```bash
git clone https://github.com/status4O4/url_shortener
cd url_shortener
````

2. **Создаем и активируем виртуальное окружение**

```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

3. **Устанавливаем зависимости**

```bash
pip install --upgrade pip
pip install -e ".[dev]"
```

---

## Конфигурация через `.env`

Создайте файл `.env` на основе примера:

```bash
cp .env.example .env
```

Пример `.env.example`:

```env
# Включение отладочного режима (логирование, авто-reload)
APP_DEBUG=true

# Путь к базе данных SQLite
APP_DATABASE_PATH=db.sqlite3

# Длина генерируемого короткого кода
APP_SHORT_CODE_LENGTH=6
```

---

## Настройка базы данных

SQLite создаётся автоматически при первом запуске приложения.
Таблица `links` создается автоматически:

---

## Запуск сервера

```bash
uvicorn app.main:app --reload
```

* `--reload` — автоматическая перезагрузка при изменениях.
* Сервер доступен по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## API

### 1. Создание короткой ссылки

**POST** `/shorten`

**Request Body:**

```json
{
  "url": "https://example.com"
}
```

**Response:**

```json
{
  "short_url": "/abc123"
}
```

---

### 2. Получение исходного URL

**GET** `/{code}`

**Response (если код найден):**
Делает редирект

**Response (если код не найден):**

```json
{
  "detail": "Not found"
}
```

---

## Тестирование

Тесты написаны с использованием `pytest`.

Запуск:

```bash
pytest -v
```
