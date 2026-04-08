import os
from pathlib import Path

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "post.jpg"

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
URL = "https://lud.su/Shafle"

POST_CAPTION = """
🚨 $100K WEEKLY RACE 🚨
🔤🔤🔤🔤  Ends May 4, 2026, 2:00 PM

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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[
        InlineKeyboardButton("▶️ Play", url=URL),
        InlineKeyboardButton("500%", url=URL),
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if not IMAGE_PATH.exists():
        await update.message.reply_text(
            f"Файл изображения не найден: {IMAGE_PATH.name}",
            reply_markup=reply_markup
        )
        return

    with open(IMAGE_PATH, "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=POST_CAPTION,
            parse_mode="HTML",
            reply_markup=reply_markup
        )

def main() -> None:
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is not set")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
