# МЯСО — Культ Продукта

Тестовый проект для отработки процессов **деплоя** и **CI/CD**.

Простой одностраничный сайт (лендинг мясного бренда), на котором отрабатываются:
- автоматический деплой на хостинг (Render);
- автоматизированное UI-тестирование (Playwright + pytest);
- (опционально) настройка CI-пайплайна, который прогоняет тесты на живом окружении после каждого деплоя.

## 🔗 Демо

Живая версия: [https://dep-projekt.onrender.com](https://dep-projekt.onrender.com)

## 📁 Структура проекта

```
.
├── .github/
│   └── workflows/
│       └── ui_tests.yml   # CI-пайплайн: прогон UI-тестов (GitHub Actions)
├── index.html             # Верстка и стили лендинга (чистый HTML/CSS, без сборки)
├── test_meat_site.py      # UI-тесты на Playwright
├── requirements.txt       # Python-зависимости (pytest, playwright и т.д.)
└── README.md
```

> `venv/`, `__pycache__/` и `.pytest_cache/` — служебные локальные папки,
> в репозиторий не коммитятся (см. `.gitignore`).

## 🛠 Стек

- **Frontend:** HTML5 + CSS3 (без фреймворков и сборщиков)
- **Тестирование:** [Playwright](https://playwright.dev/python/) + [pytest](https://docs.pytest.org/)
- **Хостинг:** [Render](https://render.com/) (static site)

## 🚀 Запуск локально

Так как проект — это статичный HTML, достаточно открыть `index.html` в браузере,
либо поднять любой локальный сервер:

```bash
python -m http.server 8000
```

и открыть [http://localhost:8000](http://localhost:8000).

## ✅ Тестирование

Тесты проверяют работоспособность **уже задеплоенной** версии сайта (`BASE_URL` в
`test_meat_site.py` указывает на прод-адрес на Render).

### Установка зависимостей

```bash
pip install pytest playwright
playwright install
```

### Запуск тестов

```bash
pytest test_meat_site.py -v
```

### Что проверяется

| Тест | Проверка |
|---|---|
| `test_site_title` | Заголовок страницы равен `М Я С О — Культ Продукта` |
| `test_logo_is_visible` | Логотип видим и содержит текст `Мясо.` |
| `test_menu_cards_count` | На странице ровно 3 карточки товаров, первая — «Рибай» |

## 🔄 CI/CD

Идея пайплайна:

1. Пуш в `main` → Render автоматически подтягивает изменения и деплоит статику.
2. После успешного деплоя запускается джоб (GitHub Actions / другой CI), который
   устанавливает Playwright и прогоняет `test_meat_site.py` против продакшн-URL,
   подтверждая, что сайт действительно поднялся и отдаёт корректный контент.

Пример шага для GitHub Actions:

```yaml
- name: Install dependencies
  run: |
    pip install pytest playwright
    playwright install --with-deps

- name: Run smoke tests against production
  run: pytest test_meat_site.py -v
```

## 📌 Заметки

- Проект учебный/тестовый — контент и данные (адрес, телефон) вымышленные.
- При изменении структуры `index.html` (классы `.logo`, `.card`, `.grid`) не забудьте
  синхронизировать селекторы в `test_meat_site.py`.