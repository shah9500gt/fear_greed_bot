from telegram import Bot
from telegram.constants import ParseMode
import requests
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Aapka bot token aur chat ID
TOKEN = "6184729036:AAHGFN2L-Jb3DfBoUuTmUPXrJ_jU_xxS0xE"
CHAT_ID = "6092997199"

async def start(update, context):
    await update.message.reply_text("Bot is alive!")

async def index(update, context):
    url = "https://api.alternative.me/fng/"
    try:
        response = requests.get(url, timeout=3)
        data = response.json()
        value = data["data"][0]["value"]
        label = data["data"][0]["value_classification"]
        msg = f"*Fear & Greed Index:* {value}\n*Status:* {label}"
        await update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)
    except:
        await update.message.reply_text("Failed to fetch data.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("index", index))
app.run_polling()
