import logging
import requests
from telegram import Update, ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '7192436665:AAFx0pqUqYC3ji9MOpb2yF8o_DFDUzImMbA'
CHAT_ID = '7203772674'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hi! Mai aapka Fear and Greed Index bot hoon.')

async def fetch_fear_greed(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        response = requests.get('https://api.alternative.me/fng/')
        data = response.json()
        value = data["data"][0]["value"]
        label = data["data"][0]["value_classification"]
        msg = f"*Fear & Greed Index:* {value}\n*Status:* {label}"
        await context.bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode=ParseMode.MARKDOWN)
    except:
        await update.message.reply_text("Data fetch karte waqt koi masla aaya.")

async def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("feargreed", fetch_fear_greed))
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
