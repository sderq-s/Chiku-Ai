import logging
import random
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# === إعداد السجلات ===
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# === توكن البوت ===
BOT_TOKEN = "7680410833:AAESNMhjnk__RSn1cwZB0Sj-4qMmqFfY3TU"

# === بيانات البوت (في الذاكرة) ===
# رصيد المستخدمين: { user_id: balance_int }
balances = {}
# تحديات الكلمات الحالية: { user_id: current_word }
challenges = {}

# قائمة الكلمات العشوائية لأمر "كلمات"
WORDS_LIST = [
    "شجاع", "مبدع", "سريع", "صادق", "متميز",
    "متعاون", "مرن", "مبتكر", "حكيم", "مرح"
]


# === /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "مرحباً! ⭐️\n"
        "أضفني كمشرف في مجموعتك ثم أرسل:\n"
        "- رصيدي\n"
        "- رصيده (رداً على رسالة أحد)\n"
        "- كلمات\n\n"
        "كل كلمة تعيد إرسالها تكسبك 20 نجمة!"
    )


# === أمر "كلمات" ===
async def send_challenge(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message
    if msg.text == "كلمات":
        word = random.choice(WORDS_LIST)
        challenges[msg.from_user.id] = word
        await msg.reply_text(
            f"أعد كتابة هذه الكلمة، وأحصل على نجوم إضافية: {word}"
        )


# === التحقق من إعادة إرسال الكلمة ===
async def check_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message
    user_id = msg.from_user.id
    text = msg.text.strip()
    # هل هناك تحدي مفتوح لهذا المستخدم؟
    if user_id in challenges and text == challenges[user_id]:
        # أكسب 20 نجمة
        balances[user_id] = balances.get(user_id, 0) + 20
        # أرسل التهنئة
        await msg.reply_text(
            "ممتاز، لقد حصلت على 20 نجمة كهدية."
        )
        # إحذف التحدي
        del challenges[user_id]


# === أوامر الرصيد ===
async def handle_balance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message
    text = msg.text.strip()
    # رصيدي
    if text == "رصيدي":
        bal = balances.get(msg.from_user.id, 0)
        await msg.reply_text(f"رصيدك: {bal} نجوم")
    # رصيده (رداً على رسالة)
    elif text == "رصيده" and msg.reply_to_message:
        target = msg.reply_to_message.from_user
        bal = balances.get(target.id, 0)
        await msg.reply_text(f"رصيده: {bal} نجوم")


def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # ترحيب
    app.add_handler(CommandHandler("start", start))
    # إرسال تحدي "كلمات"
    app.add_handler(MessageHandler(
        filters.TEXT & filters.ChatType.SUPERGROUP, send_challenge
    ))
    # التحقق من إجابة التحدي
    app.add_handler(MessageHandler(
        filters.TEXT & filters.ChatType.SUPERGROUP, check_answer
    ))
    # أوامر الرصيد
    app.add_handler(MessageHandler(
        filters.TEXT & filters.ChatType.SUPERGROUP, handle_balance
    ))

    logger.info("البوت يعمل الآن...")
    app.run_polling()


if __name__ == "__main__":
    main()
