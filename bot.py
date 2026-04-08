import os
import logging
from pathlib import Path

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "post.jpg"

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
URL = "https://lud.su/Shafle"

POST_CAPTION = """
🚨 $100K WEEKLY RACE 🚨
Ends May 4, 2026, 2:00 PM

💰 Up to $25,000 for #1
🔥 Bet & climb — no signup needed
📈 More volume = higher rank

🏆 Top 1000 get paid
⚡️ Live leaderboard

👉 Join now: https://lud.su/Shafle

💥 Grind hard. Get paid weekly.

🔥 Hot deal from Shuffle

🎁 100% First Deposit Bonus — double your balance instantly 💰

⏳ Limited access, don’t miss out 🔗 <a href="https://lud.su/Shafle">Claim here</a>
"""

def build_keyboard() -> InlineKeyboardMarkup:
    keyboard = [[
        InlineKeyboardButton("▶️ Play", url=URL),
        InlineKeyboardButton("500%", url=URL),
    ]]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return

    reply_markup = build_keyboard()

    if not IMAGE_PATH.exists():
        await update.message.reply_text(
            "Файл post.jpg не найден в корне репозитория.",
            reply_markup=reply_markup,
        )
        return

    with open(IMAGE_PATH, "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=POST_CAPTION,
            parse_mode="HTML",
            reply_markup=reply_markup,
        )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.exception("Exception while handling an update:", exc_info=context.error)

def main() -> None:
    if not TOKEN:
        raise ValueError("Переменная окружения TELEGRAM_BOT_TOKEN не задана")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_error_handler(error_handler)

    app.run_polling()

if __name__ == "__main__":
    main()
