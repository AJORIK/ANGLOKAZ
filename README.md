# Telegram bot for Railway

## Что делает бот
- По команде `/start` отправляет один пост с картинкой
- Под постом показывает 2 кнопки:
  - `▶️ Play`
  - `500%`
- Обе кнопки ведут на одну и ту же ссылку: `https://lud.su/Shafle`

## Как запустить через Railway
1. Создай бота через `@BotFather`
2. Залей этот проект в GitHub
3. Подключи репозиторий в Railway
4. В Railway -> Variables добавь:
   - `TELEGRAM_BOT_TOKEN`
5. Deploy

## Локальный запуск
```bash
pip install -r requirements.txt
export TELEGRAM_BOT_TOKEN=your_token
python bot.py
```
