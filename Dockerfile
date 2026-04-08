import logging
import os
from pathlib import Path

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
BUTTON_URL = 'https://lud.su/Shafle'
MEDIA_PATH = Path(__file__).resolve().parent / 'assets' / 'post.jpg'

POST_CAPTION = """🚨 $100K WEEKLY RACE 🚨
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

⏳ Limited access, don’t miss out 🔗 <a href=\"https://lud.su/Shafle\">Claim here</a>!!!"""


def build_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('▶️ Play', url=BUTTON_URL),
            InlineKeyboardButton('500%', url=BUTTON_URL),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message is None:
        return

    if MEDIA_PATH.exists():
        with MEDIA_PATH.open('rb') as photo:
            await message.reply_photo(
                photo=photo,
                caption=POST_CAPTION,
                parse_mode='HTML',
                reply_markup=build_keyboard(),
            )
    else:
        await message.reply_text(
            text=POST_CAPTION,
            parse_mode='HTML',
            reply_markup=build_keyboard(),
            disable_web_page_preview=False,
        )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error('Exception while handling an update:', exc_info=context.error)


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError('Переменная окружения TELEGRAM_BOT_TOKEN не задана')

    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_error_handler(error_handler)

    logger.info('Bot started')
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
