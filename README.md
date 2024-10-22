# Mook_Ltd_test
Instant messaging service


Инициализировать Alembic в директории migrations
`alembic init --template async migrations`

Автоматическое создание миграций c комментарием "First migration"
`alembic revision --autogenerate -m "First migration"`

Применение миграций
`alembic upgrade head`

1. Поменять драйвер aiosqlite на движок для работы с Postgress
