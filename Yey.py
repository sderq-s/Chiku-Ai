import logging
import random
import re
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7680410833:AAESNMhjnk__RSn1cwZB0Sj-4qMmqFfY3TU"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

balances = {}       # {user_id: balance}
challenges = {}     # {user_id: current_word}

WORDS_LIST = [
    "شجاع", "ذكي", "سريع", "جميل", "صادق", "مميز", "مذهل", "قوي", "لطيف",
    "مرح", "هادئ", "عالي", "مشرق", "نقي", "كبير", "صغير", "مفيد", "بارع",
    "مبتسم", "سعيد", "كريم", "طموح", "هادف", "مرن", "مخترع", "مؤدب", "عبقري",
    "محترف", "ذووق", "وسيم", "ذوّاق", "متألق"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحباً بك! ⭐\n"
        "- أرسل 'كلمات' لتربح نجوم.\n"
        "- أرسل 'رصيدي' لمعرفة رصيدك.\n"
        "- أرسل 'رصيده' رداً على رسالة أحد لمعرفة رصيده.\n"
        "- أرسل: إرسال 20 نجوم، رداً على صديقك لإرسال له النجوم."
    )

async def words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    word = random.choice(WORDS_LIST)
    challenges[user_id] = word
    await update.message.reply_text(
        f"أعد إرسال الكلمة التالية وأحصل على نجوم إضافية: {word}"
    )

async def check_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text.strip()
    word = challenges.get(user_id)

    if word and text == word:
        balances[user_id] = balances.get(user_id, 0) + 20
        del challenges[user_id]
        await update.message.reply_text("ممتاز! لقد فزت بـ20 نجمة.")

async def my_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.strip() == "رصيدي":
        user_id = update.message.from_user.id
        bal = balances.get(user_id, 0)
        await update.message.reply_text(f"رصيدك: {bal} نجوم")

async def his_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if msg.text.strip() == "رصيده" and msg.reply_to_message:
        target = msg.reply_to_message.from_user
        if target.is_bot:
            return
        bal = balances.get(target.id, 0)
        await msg.reply_text(f"رصيده: {bal} نجوم")

async def send_stars(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg.reply_to_message or msg.reply_to_message.from_user.is_bot:
        return

    text = msg.text.strip()
    match = re.match(r"إرسال\s+(\d+)\s+نجوم", text)
    if match:
        amount = int(match.group(1))
        sender_id = msg.from_user.id
        receiver_id = msg.reply_to_message.from_user.id

        if balances.get(sender_id, 0) < amount:
            await msg.reply_text("مهلاً، لا يوجد لديك رصيد كافي لإكمال هذه العملية.")
        else:
            balances[sender_id] -= amount
            balances[receiver_id] = balances.get(receiver_id, 0) + amount
            await msg.reply_text("نجاح! لقد تم إرسال نجومك إلى رفيقك.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, words))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, check_word))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, my_balance))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, his_balance))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, send_stars))

    logger.info("البوت يعمل الآن...")
    app.run_polling()

if __name__ == "__main__":
    main()
