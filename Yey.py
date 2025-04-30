import logging
import random
import re
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = "7680410833:AAESNMhjnk__RSn1cwZB0Sj-4qMmqFfY3TU"

# === السجلات ===
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# === تخزين البيانات ===
balances = {}     # {user_id: النجوم}
challenges = {}   # {user_id: (الكلمة)}

# === الكلمات العشوائية ===
WORDS = [
    "شجاع", "ذكي", "قوي", "لطيف", "مرح", "سعيد", "كريم", "مبتسم", "سريع", "مشرق",
    "نقي", "كبير", "بارع", "محترف", "عبقري", "وسيم", "مؤدب", "طموح", "مذهل", "جميل",
    "هادئ", "نشيط", "متواضع", "مفيد", "صادق", "خجول", "نادر", "ذوّاق", "حنون", "ذوّوق"
]

# === /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحباً بك في بوت النجوم ⭐️\n\n"
        "- أرسل 'كلمات' لربح النجوم.\n"
        "- أرسل 'رصيدي' لمعرفة رصيدك.\n"
        "- أرسل 'رصيده' رداً على أحد لرؤية رصيده.\n"
        "- أرسل 'إرسال 10 نجوم' رداً على أحد لتحويل النجوم."
    )


# === أمر: كلمات ===
async def handle_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    word = random.choice(WORDS)
    challenges[user_id] = word
    await update.message.reply_text(
        f"أعد إرسال الكلمة التالية وأحصل على نجوم إضافية: {word}"
    )


# === تحقق من الكلمات ===
async def check_challenge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    msg = update.message.text.strip()

    if user_id in challenges:
        target_word = challenges[user_id]
        if msg == target_word:
            balances[user_id] = balances.get(user_id, 0) + 20
            del challenges[user_id]
            await update.message.reply_text("ممتاز! لقد فزت بـ20 نجمة.")


# === رصيدي ===
async def handle_my_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.strip() == "رصيدي":
        user_id = update.message.from_user.id
        bal = balances.get(user_id, 0)
        await update.message.reply_text(f"رصيدك: {bal} نجوم")


# === رصيده ===
async def handle_his_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if msg.text.strip() == "رصيده" and msg.reply_to_message:
        target = msg.reply_to_message.from_user
        if target.is_bot:
            return
        bal = balances.get(target.id, 0)
        await update.message.reply_text(f"رصيده: {bal} نجوم")


# === تحويل النجوم ===
async def handle_transfer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg.reply_to_message or msg.reply_to_message.from_user.is_bot:
        return

    pattern = r"إرسال (\d+) نجوم"
    match = re.match(pattern, msg.text.strip())
    if match:
        amount = int(match.group(1))
        sender_id = msg.from_user.id
        receiver_id = msg.reply_to_message.from_user.id

        sender_balance = balances.get(sender_id, 0)
        if sender_balance >= amount:
            balances[sender_id] = sender_balance - amount
            balances[receiver_id] = balances.get(receiver_id, 0) + amount
            await msg.reply_text("نجاح! لقد تم إرسال نجومك إلى رفيقك.")
        else:
            await msg.reply_text("مهلاً، لا يوجد لديك رصيد كافي لإكمال هذه العملية.")


# === ربط كل شيء ===
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, handle_words))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, check_challenge))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, handle_my_balance))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, handle_his_balance))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, handle_transfer))

    logger.info("البوت يعمل الآن...")
    app.run_polling()


if __name__ == "__main__":
    main()
