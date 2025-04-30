import logging
import random
from telegram import Update, ChatMember
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# === التوكن ===
BOT_TOKEN = "7680410833:AAESNMhjnk__RSn1cwZB0Sj-4qMmqFfY3TU"

# === سجلات ===
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# === تخزين بيانات المستخدمين ===
balances = {}       # {user_id: balance}
challenges = {}     # {user_id: current_word}

# === قائمة طويلة من الكلمات ===
WORDS_LIST = [
    "شجاع", "ذكي", "سريع", "جميل", "صادق", "مميز", "مذهل", "قوي", "لطيف",
    "مرح", "هادئ", "عالي", "مشرق", "نقي", "كبير", "صغير", "مفيد", "بارع",
    "مبتسم", "سعيد", "كريم", "طموح", "هادف", "مرن", "مخترع", "مؤدب", "عبقري",
    "محترف", "ذووق", "وسيم", "ذوّاق", "متألق"
]

# === /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحباً بك! ⭐\n"
        "- أرسل 'كلمات' لتربح نجوم.\n"
        "- أرسل 'رصيدي' لمعرفة رصيدك.\n"
        "- أرسل 'رصيده' رداً على رسالة أحد لمعرفة رصيده.\n\n"
        "أعد كتابة الكلمة لتحصل على 20 نجمة!"
    )


# === كلمات ===
async def words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    word = random.choice(WORDS_LIST)
    challenges[user_id] = word
    await update.message.reply_text(
        f"أعد كتابة هذه الكلمة، وأحصل على نجوم إضافية: {word}"
    )


# === تحقق من إجابة صحيحة ===
async def check_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text.strip()
    if user_id in challenges and text == challenges[user_id]:
        balances[user_id] = balances.get(user_id, 0) + 20
        del challenges[user_id]
        await update.message.reply_text("ممتاز! لقد فزت بـ20 نجمة.")


# === رصيدي ===
async def my_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.strip() == "رصيدي":
        user_id = update.message.from_user.id
        bal = balances.get(user_id, 0)
        await update.message.reply_text(f"رصيدك: {bal} نجوم")


# === رصيده ===
async def his_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if msg.text.strip() == "رصيده" and msg.reply_to_message:
        target = msg.reply_to_message.from_user
        if target.is_bot:
            return  # تجاهل الرد على بوتات
        bal = balances.get(target.id, 0)
        await msg.reply_text(f"رصيده: {bal} نجوم")


# === دمج كل شيء ===
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, words))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, check_word))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, my_balance))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, his_balance))

    logger.info("البوت يعمل الآن...")
    app.run_polling()


if __name__ == "__main__":
    main()
