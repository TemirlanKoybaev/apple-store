# Apple Store (Django) — учебный проект

Учебное веб-приложение на Django в формате командной разработки (3 человека).

## Функциональность
- Каталог товаров: категории, поиск, сортировка по цене, пагинация
- Страница товара (detail)
- Корзина (Django sessions) — добавление/удаление/изменение количества, итоговая сумма
- Страницы: Контакты (черновик)

## Технологии
- Python 3.x
- Django
- SQLite (dev)

## Установка и запуск (локально)
```bash
python -m venv .venv
# Windows:
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
